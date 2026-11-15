"""Test suite. Each test docstring = 'ID | description | expected result' (used for the report table)."""
import base64, hashlib, io, json, logging, os, tempfile, unittest
from unittest import mock
from sdsp import core
from sdsp.core import (WrongKeyError, TamperedPackageError, MalformedPackageError,
                       UnsupportedInputError, SDSPError)

PW = b"correct horse battery staple"


def flip_bit(pkg: bytes, field: str, byte=0, bit=0) -> bytes:
    obj = json.loads(pkg)
    raw = bytearray(base64.b64decode(obj[field]))
    raw[byte] ^= 1 << bit
    obj[field] = base64.b64encode(bytes(raw)).decode()
    return json.dumps(obj).encode()


class T(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a_priv, cls.a_pub = core.generate_keypair(PW)        # intended recipient
        cls.b_priv, cls.b_pub = core.generate_keypair(None)      # a different user

    def enc(self, data=b"Exam paper: confidential", name="exam.txt"):
        return core.encrypt_bytes(data, self.a_pub, name)

    # ---- minimum test plan 1-6 (from the project brief)
    def test_01_valid_roundtrip(self):
        """T1 | Valid recipient decrypts; bytes and SHA-256 equal original | ACCEPT, identical"""
        data = os.urandom(10_000)
        out, name = core.decrypt_bytes(self.enc(data, "a.bin"), self.a_priv, PW)
        self.assertEqual(out, data)
        self.assertEqual(hashlib.sha256(out).digest(), hashlib.sha256(data).digest())
        self.assertEqual(name, "a.bin")

    def test_02_wrong_private_key(self):
        """T2 | A different user's private key tries to open the package | REJECT (wrong key)"""
        with self.assertRaises(WrongKeyError):
            core.decrypt_bytes(self.enc(), self.b_priv, None)

    def test_02b_wrong_passphrase(self):
        """T2b | Correct key file but wrong passphrase | REJECT (wrong key)"""
        with self.assertRaises(WrongKeyError):
            core.decrypt_bytes(self.enc(), self.a_priv, b"wrong")

    def test_03_ciphertext_bit_flip(self):
        """T3a | Flip 1 bit in ciphertext | REJECT (tampered)"""
        with self.assertRaises(TamperedPackageError):
            core.decrypt_bytes(flip_bit(self.enc(), "ciphertext", 3, 5), self.a_priv, PW)

    def test_03b_tag_bit_flip(self):
        """T3b | Flip 1 bit in authentication tag | REJECT (tampered)"""
        with self.assertRaises(TamperedPackageError):
            core.decrypt_bytes(flip_bit(self.enc(), "tag", 0, 0), self.a_priv, PW)

    def test_04a_nonce_modified(self):
        """T4a | Flip 1 bit in nonce | REJECT (tampered)"""
        with self.assertRaises(TamperedPackageError):
            core.decrypt_bytes(flip_bit(self.enc(), "nonce", 0, 0), self.a_priv, PW)

    def test_04b_header_modified(self):
        """T4b | Change filename in header (bound as AAD) | REJECT (tampered)"""
        obj = json.loads(self.enc()); obj["filename"] = "grades.txt"
        with self.assertRaises(TamperedPackageError):
            core.decrypt_bytes(json.dumps(obj).encode(), self.a_priv, PW)

    def test_04c_wrapped_key_modified(self):
        """T4c | Flip 1 bit in RSA-wrapped key | REJECT (wrong key / modified key block)"""
        with self.assertRaises(SDSPError):
            core.decrypt_bytes(flip_bit(self.enc(), "wrapped_key", 10, 2), self.a_priv, PW)

    def test_04d_malformed_inputs(self):
        """T4d | Garbage, non-JSON, missing field, bad base64, short nonce | REJECT (malformed)"""
        good = json.loads(self.enc())
        cases = [b"\x00\xff garbage", b"[]", b"{}"]
        d = dict(good); del d["tag"]; cases.append(json.dumps(d).encode())
        d = dict(good); d["ciphertext"] = "***not base64***"; cases.append(json.dumps(d).encode())
        d = dict(good); d["nonce"] = base64.b64encode(b"short").decode(); cases.append(json.dumps(d).encode())
        for c in cases:
            with self.assertRaises(MalformedPackageError):
                core.decrypt_bytes(c, self.a_priv, PW)

    def test_04e_unsupported_version(self):
        """T4e | Unknown package version / algorithm suite | REJECT (unsupported)"""
        for k, v in (("version", 99), ("aead", "DES-CBC"), ("format", "ZIP")):
            obj = json.loads(self.enc()); obj[k] = v
            with self.assertRaises(UnsupportedInputError):
                core.decrypt_bytes(json.dumps(obj).encode(), self.a_priv, PW)

    def test_05a_empty_file(self):
        """T5a | Empty (0-byte) file | ACCEPT, round-trips"""
        self.assertEqual(core.decrypt_bytes(self.enc(b""), self.a_priv, PW)[0], b"")

    def test_05b_large_file(self):
        """T5b | 5 MB binary file | ACCEPT, identical bytes"""
        data = os.urandom(5 * 1024 * 1024)
        self.assertEqual(core.decrypt_bytes(self.enc(data), self.a_priv, PW)[0], data)

    def test_05c_text_pdf_image_types(self):
        """T5c | Unicode text, PDF-like and PNG-like binary content | ACCEPT, identical"""
        for blob in ("سلام دنیا – امتحان 🔐".encode(), b"%PDF-1.7\n" + os.urandom(2000),
                     b"\x89PNG\r\n\x1a\n" + os.urandom(3000)):
            self.assertEqual(core.decrypt_bytes(self.enc(blob), self.a_priv, PW)[0], blob)

    def test_06_no_secrets_in_logs(self):
        """T6 | Debug logs during encrypt/decrypt/failures contain no plaintext or key material | NONE found"""
        stream = io.StringIO(); h = logging.StreamHandler(stream)
        lg = logging.getLogger("sdsp"); lg.addHandler(h); lg.setLevel(logging.DEBUG)
        marker = b"TOP-SECRET-MARKER-12345"; seen = []
        real = core.AESGCM.generate_key
        def spy(*a, **k):
            key = real(*a, **k); seen.append(key); return key
        try:
            with mock.patch.object(core.AESGCM, "generate_key", staticmethod(spy)):
                pkg = self.enc(marker)
            core.decrypt_bytes(pkg, self.a_priv, PW)
            with self.assertRaises(SDSPError):
                core.decrypt_bytes(pkg, self.b_priv, None)
        finally:
            lg.removeHandler(h)
        text = stream.getvalue()
        self.assertTrue(text)  # something was logged
        for secret in (marker.decode(), "PRIVATE KEY", PW.decode(), seen[0].hex(),
                       base64.b64encode(seen[0]).decode()):
            self.assertNotIn(secret, text)

    # ---- additional security properties
    def test_07_fresh_key_and_nonce(self):
        """T7 | Same file encrypted twice | different nonce, wrapped key, ciphertext"""
        a, b = json.loads(self.enc()), json.loads(self.enc())
        for f in ("nonce", "wrapped_key", "ciphertext"):
            self.assertNotEqual(a[f], b[f])

    def test_08_package_has_no_secrets(self):
        """T8 | Package contains no plaintext and no private-key material | NONE found"""
        pkg = self.enc(b"PLAINTEXT-MARKER-XYZ")
        self.assertNotIn(b"PLAINTEXT-MARKER-XYZ", pkg); self.assertNotIn(b"PRIVATE", pkg)

    def test_09_no_output_on_failure(self):
        """T9 | Failed decryption writes NO plaintext file to disk | no file created"""
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "x.sdsp")
            open(p, "wb").write(flip_bit(self.enc(), "ciphertext"))
            kp = os.path.join(d, "k.pem"); open(kp, "wb").write(self.a_priv)
            with self.assertRaises(TamperedPackageError):
                core.decrypt_file(p, kp, os.path.join(d, "out"), PW)
            self.assertFalse(os.path.exists(os.path.join(d, "out", "exam.txt")))

    def test_10_path_traversal_filename(self):
        """T10 | Filename '../../evil.txt' in package | saved only as basename"""
        pkg = core.encrypt_bytes(b"x", self.a_pub, "../../evil.txt")
        self.assertEqual(core.decrypt_bytes(pkg, self.a_priv, PW)[1], "evil.txt")

    def test_11_weak_or_bad_keys_refused(self):
        """T11 | 1024-bit RSA request / garbage public key | REJECT (unsupported)"""
        with self.assertRaises(UnsupportedInputError): core.generate_keypair(None, bits=1024)
        with self.assertRaises(UnsupportedInputError): core.encrypt_bytes(b"x", b"not a key")

    def test_12_file_workflow(self):
        """T12 | encrypt_file -> decrypt_file on disk; refuses to overwrite | ACCEPT, then REJECT overwrite"""
        with tempfile.TemporaryDirectory() as d:
            src = os.path.join(d, "report.pdf"); open(src, "wb").write(b"%PDF" + os.urandom(500))
            pub, priv = os.path.join(d, "p.pem"), os.path.join(d, "s.pem")
            open(pub, "wb").write(self.a_pub); open(priv, "wb").write(self.a_priv)
            pkg = core.encrypt_file(src, pub, src + ".sdsp")
            out = core.decrypt_file(pkg, priv, os.path.join(d, "o"), PW)
            self.assertEqual(open(out, "rb").read(), open(src, "rb").read())
            with self.assertRaises(UnsupportedInputError):
                core.decrypt_file(pkg, priv, os.path.join(d, "o"), PW)


if __name__ == "__main__":
    unittest.main()
