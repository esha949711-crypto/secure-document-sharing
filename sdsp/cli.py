"""Command-line interface:  python -m sdsp.cli {keygen|encrypt|decrypt|fingerprint} ..."""
import argparse
import getpass
import os
import sys

from . import core


def _pass(prompt: str, confirm=False):
    p = getpass.getpass(prompt)
    if confirm and p != getpass.getpass("Repeat passphrase: "):
        print("[ERROR] Passphrases do not match."); sys.exit(2)
    return p.encode() if p else None


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="sdsp", description="Secure Document Sharing Prototype (educational)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    k = sub.add_parser("keygen", help="create an RSA key pair"); k.add_argument("--name", required=True)
    k.add_argument("--dir", default="keys")
    e = sub.add_parser("encrypt", help="encrypt a file for a recipient")
    e.add_argument("--in", dest="inp", required=True); e.add_argument("--pub", required=True)
    e.add_argument("--out")
    d = sub.add_parser("decrypt", help="decrypt a package"); d.add_argument("--in", dest="inp", required=True)
    d.add_argument("--priv", required=True); d.add_argument("--outdir", default="decrypted")
    d.add_argument("--force", action="store_true")
    f = sub.add_parser("fingerprint", help="print a public key fingerprint"); f.add_argument("--pub", required=True)
    a = ap.parse_args(argv)
    try:
        if a.cmd == "keygen":
            os.makedirs(a.dir, exist_ok=True)
            priv, pub = core.generate_keypair(_pass("Passphrase for private key (empty = none): ", True))
            pp, pu = os.path.join(a.dir, a.name + ".private.pem"), os.path.join(a.dir, a.name + ".public.pem")
            fd = os.open(pp, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            with os.fdopen(fd, "wb") as fh: fh.write(priv)
            with open(pu, "wb") as fh: fh.write(pub)
            print(f"[SUCCESS] Keys written: {pp} (KEEP SECRET), {pu} (share this)")
            print("Public key fingerprint (verify out-of-band):", core.fingerprint(pub))
        elif a.cmd == "encrypt":
            out = a.out or a.inp + ".sdsp"
            core.encrypt_file(a.inp, a.pub, out)
            print(f"[SUCCESS] Encrypted package written: {out}")
        elif a.cmd == "decrypt":
            with open(a.priv, "rb") as fh: needs_pw = b"ENCRYPTED" in fh.read()
            pw = _pass("Private key passphrase: ") if needs_pw else None
            out = core.decrypt_file(a.inp, a.priv, a.outdir, pw, a.force)
            print(f"[SUCCESS] Authenticated and decrypted: {out}")
        elif a.cmd == "fingerprint":
            with open(a.pub, "rb") as fh: print(core.fingerprint(fh.read()))
        return 0
    except core.SDSPError as exc:
        print(f"[{exc.status}] {exc}"); return 1
    except FileExistsError as exc:
        print(f"[UNSUPPORTED INPUT] {exc.filename} already exists"); return 1


if __name__ == "__main__":
    sys.exit(main())
