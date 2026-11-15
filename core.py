"""
Core of the Secure Document Sharing Prototype (SDSP).

Design (hybrid encryption):
  1. A fresh random 256-bit AES key (the data-encryption key, DEK) is made per file.
  2. The file is protected with AES-256-GCM using a fresh random 96-bit nonce.
  3. The DEK is wrapped for the recipient with RSA-OAEP (SHA-256, MGF1-SHA-256).
  4. The package header AND the wrapped key are bound to the ciphertext as GCM
     associated data (AAD), so any change to them makes authentication fail.
  5. The receiver unwraps the DEK with the private key and releases plaintext ONLY
     after the GCM tag verifies.

All real cryptography comes from the `cryptography` library (no home-made ciphers).
Educational prototype: see README for limitations.
"""
import base64
import binascii
import hashlib
import json
import logging
import os
from typing import Optional, Tuple

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

log = logging.getLogger("sdsp")  # NEVER log plaintext, keys, or passphrases.

FORMAT = "SDSP"
VERSION = 1
AEAD_NAME = "AES-256-GCM"
KEM_NAME = "RSA-OAEP-SHA256"
RSA_BITS = 3072
KEY_LEN = 32      # AES-256
NONCE_LEN = 12    # 96-bit nonce, the size recommended for GCM
TAG_LEN = 16      # 128-bit tag
MAX_FILE_BYTES = 256 * 1024 * 1024  # in-memory prototype limit

_REQUIRED = ("format", "version", "aead", "kem", "recipient_fp", "filename",
             "wrapped_key", "nonce", "ciphertext", "tag")


# ---------------------------------------------------------------- exceptions
class SDSPError(Exception):
    """Base class; `status` is the user-facing status label."""
    status = "ERROR"


class WrongKeyError(SDSPError):
    status = "WRONG KEY"


class TamperedPackageError(SDSPError):
    status = "CORRUPTED / MODIFIED FILE"


class MalformedPackageError(SDSPError):
    status = "MALFORMED PACKAGE"


class UnsupportedInputError(SDSPError):
    status = "UNSUPPORTED INPUT"


# ---------------------------------------------------------------------- keys
def generate_keypair(passphrase: Optional[bytes] = None,
                     bits: int = RSA_BITS) -> Tuple[bytes, bytes]:
    """Return (private_pem, public_pem). Private key is encrypted if a passphrase is given."""
    if bits < 2048:
        raise UnsupportedInputError("RSA key size below 2048 bits is not allowed.")
    key = rsa.generate_private_key(public_exponent=65537, key_size=bits)
    enc = (serialization.BestAvailableEncryption(passphrase)
           if passphrase else serialization.NoEncryption())
    priv = key.private_bytes(serialization.Encoding.PEM,
                             serialization.PrivateFormat.PKCS8, enc)
    pub = key.public_key().public_bytes(
        serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
    return priv, pub


def _load_public(pem: bytes) -> rsa.RSAPublicKey:
    try:
        key = serialization.load_pem_public_key(pem)
    except (ValueError, TypeError) as exc:
        raise UnsupportedInputError("Not a valid PEM public key.") from exc
    if not isinstance(key, rsa.RSAPublicKey):
        raise UnsupportedInputError("Only RSA public keys are supported.")
    if key.key_size < 2048:
        raise UnsupportedInputError("RSA key too small (minimum 2048 bits).")
    return key


def _load_private(pem: bytes, passphrase: Optional[bytes]) -> rsa.RSAPrivateKey:
    try:
        key = serialization.load_pem_private_key(pem, password=passphrase or None)
    except (ValueError, TypeError) as exc:
        # wrong passphrase, missing passphrase, or not a PEM private key
        raise WrongKeyError("Private key could not be loaded (bad PEM or wrong passphrase).") from exc
    if not isinstance(key, rsa.RSAPrivateKey):
        raise UnsupportedInputError("Only RSA private keys are supported.")
    return key


def fingerprint(pub) -> str:
    """SHA-256 fingerprint of the DER SubjectPublicKeyInfo (accepts PEM bytes or key object)."""
    if isinstance(pub, (bytes, bytearray)):
        pub = _load_public(bytes(pub))
    der = pub.public_bytes(serialization.Encoding.DER,
                           serialization.PublicFormat.SubjectPublicKeyInfo)
    return hashlib.sha256(der).hexdigest()


# ------------------------------------------------------------------- helpers
def _b64e(b: bytes) -> str:
    return base64.b64encode(b).decode("ascii")


def _b64d(s, field: str, exact_len: Optional[int] = None) -> bytes:
    if not isinstance(s, str):
        raise MalformedPackageError(f"Field '{field}' must be a string.")
    try:
        raw = base64.b64decode(s.encode("ascii"), validate=True)
    except (binascii.Error, UnicodeEncodeError) as exc:
        raise MalformedPackageError(f"Field '{field}' is not valid base64.") from exc
    if exact_len is not None and len(raw) != exact_len:
        raise MalformedPackageError(f"Field '{field}' has wrong length.")
    return raw


def _aad(header: dict) -> bytes:
    """Canonical associated data: everything security-relevant except the ciphertext/tag."""
    fields = {k: header[k] for k in
              ("format", "version", "aead", "kem", "recipient_fp", "filename", "wrapped_key", "nonce")}
    return json.dumps(fields, sort_keys=True, separators=(",", ":")).encode("utf-8")


# ---------------------------------------------------------------- encryption
def encrypt_bytes(data: bytes, recipient_public_pem: bytes, filename: str = "") -> bytes:
    """Encrypt `data` for the recipient; returns the package as UTF-8 JSON bytes."""
    if not isinstance(data, (bytes, bytearray)):
        raise UnsupportedInputError("Input must be bytes.")
    if len(data) > MAX_FILE_BYTES:
        raise UnsupportedInputError("File too large for this prototype (limit 256 MB).")
    pub = _load_public(recipient_public_pem)

    dek = AESGCM.generate_key(bit_length=256)        # fresh key per file (OS CSPRNG)
    nonce = os.urandom(NONCE_LEN)                    # fresh nonce per file (OS CSPRNG)
    wrapped = pub.encrypt(dek, padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(), label=None))

    header = {
        "format": FORMAT, "version": VERSION, "aead": AEAD_NAME, "kem": KEM_NAME,
        "recipient_fp": fingerprint(pub),
        "filename": os.path.basename(filename or ""),
        "wrapped_key": _b64e(wrapped), "nonce": _b64e(nonce),
    }
    sealed = AESGCM(dek).encrypt(nonce, bytes(data), _aad(header))
    header["ciphertext"] = _b64e(sealed[:-TAG_LEN])
    header["tag"] = _b64e(sealed[-TAG_LEN:])
    log.info("Encrypted %d bytes for recipient %s", len(data), header["recipient_fp"][:16])
    return json.dumps(header, indent=2).encode("utf-8")


# ---------------------------------------------------------------- decryption
def _parse_package(package: bytes) -> dict:
    try:
        obj = json.loads(package.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise MalformedPackageError("Package is not valid SDSP JSON.") from exc
    if not isinstance(obj, dict):
        raise MalformedPackageError("Package root must be an object.")
    missing = [f for f in _REQUIRED if f not in obj]
    if missing:
        raise MalformedPackageError("Missing required field(s): " + ", ".join(missing))
    if obj["format"] != FORMAT:
        raise UnsupportedInputError("Not an SDSP package.")
    if obj["version"] != VERSION:
        raise UnsupportedInputError(f"Unsupported package version: {obj['version']!r}.")
    if obj["aead"] != AEAD_NAME or obj["kem"] != KEM_NAME:
        raise UnsupportedInputError("Unsupported algorithm suite.")
    for f in ("recipient_fp", "filename"):
        if not isinstance(obj[f], str):
            raise MalformedPackageError(f"Field '{f}' must be a string.")
    return obj


def decrypt_bytes(package: bytes, private_pem: bytes,
                  passphrase: Optional[bytes] = None) -> Tuple[bytes, str]:
    """Return (plaintext, filename). Plaintext is returned only if authentication succeeds."""
    obj = _parse_package(package)
    nonce = _b64d(obj["nonce"], "nonce", NONCE_LEN)
    tag = _b64d(obj["tag"], "tag", TAG_LEN)
    ciphertext = _b64d(obj["ciphertext"], "ciphertext")
    wrapped = _b64d(obj["wrapped_key"], "wrapped_key")

    priv = _load_private(private_pem, passphrase)
    if fingerprint(priv.public_key()) != obj["recipient_fp"]:
        raise WrongKeyError("This package was addressed to a different recipient key.")
    try:
        dek = priv.decrypt(wrapped, padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(), label=None))
    except ValueError as exc:
        raise WrongKeyError("Could not recover the data key (wrong key or modified key block).") from exc
    if len(dek) != KEY_LEN:
        raise TamperedPackageError("Recovered data key has an invalid length.")
    try:
        plaintext = AESGCM(dek).decrypt(nonce, ciphertext + tag, _aad(obj))
    except InvalidTag as exc:
        raise TamperedPackageError("Authentication failed: file or header was modified.") from exc
    log.info("Decrypted %d bytes (authentication OK)", len(plaintext))
    return plaintext, os.path.basename(obj["filename"])


# ------------------------------------------------------------- file helpers
def encrypt_file(in_path: str, public_key_path: str, out_path: str) -> str:
    try:
        with open(in_path, "rb") as f:
            data = f.read(MAX_FILE_BYTES + 1)
        with open(public_key_path, "rb") as f:
            pub = f.read()
    except OSError as exc:
        raise UnsupportedInputError(f"Cannot read input: {exc.strerror}") from exc
    pkg = encrypt_bytes(data, pub, os.path.basename(in_path))
    with open(out_path, "wb") as f:
        f.write(pkg)
    return out_path


def decrypt_file(package_path: str, private_key_path: str, out_dir: str,
                 passphrase: Optional[bytes] = None, overwrite: bool = False) -> str:
    """Writes the output file only after successful authentication."""
    try:
        with open(package_path, "rb") as f:
            pkg = f.read()
        with open(private_key_path, "rb") as f:
            priv = f.read()
    except OSError as exc:
        raise UnsupportedInputError(f"Cannot read input: {exc.strerror}") from exc
    data, name = decrypt_bytes(pkg, priv, passphrase)
    name = name or "decrypted_file"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, name)
    if os.path.exists(out_path) and not overwrite:
        raise UnsupportedInputError(f"Refusing to overwrite existing file: {out_path}")
    with open(out_path, "wb") as f:
        f.write(data)
    return out_path
