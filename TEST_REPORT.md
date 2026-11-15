# Test Report

- Date: 2026-11-15  |  Python 3.13.14  |  cryptography 50.0.2
- Result: **20/20 passed**

| ID | Test | Expected | Actual |
|---|---|---|---|
| T1 | Valid recipient decrypts; bytes and SHA-256 equal original | ACCEPT, identical | PASS |
| T2 | A different user's private key tries to open the package | REJECT (wrong key) | PASS |
| T2b | Correct key file but wrong passphrase | REJECT (wrong key) | PASS |
| T3a | Flip 1 bit in ciphertext | REJECT (tampered) | PASS |
| T3b | Flip 1 bit in authentication tag | REJECT (tampered) | PASS |
| T4a | Flip 1 bit in nonce | REJECT (tampered) | PASS |
| T4b | Change filename in header (bound as AAD) | REJECT (tampered) | PASS |
| T4c | Flip 1 bit in RSA-wrapped key | REJECT (wrong key / modified key block) | PASS |
| T4d | Garbage, non-JSON, missing field, bad base64, short nonce | REJECT (malformed) | PASS |
| T4e | Unknown package version / algorithm suite | REJECT (unsupported) | PASS |
| T5a | Empty (0-byte) file | ACCEPT, round-trips | PASS |
| T5b | 5 MB binary file | ACCEPT, identical bytes | PASS |
| T5c | Unicode text, PDF-like and PNG-like binary content | ACCEPT, identical | PASS |
| T6 | Debug logs during encrypt/decrypt/failures contain no plaintext or key material | NONE found | PASS |
| T7 | Same file encrypted twice | different nonce, wrapped key, ciphertext | PASS |
| T8 | Package contains no plaintext and no private-key material | NONE found | PASS |
| T9 | Failed decryption writes NO plaintext file to disk | no file created | PASS |
| T10 | Filename '../../evil.txt' in package | saved only as basename | PASS |
| T11 | 1024-bit RSA request / garbage public key | REJECT (unsupported) | PASS |
| T12 | encrypt_file -> decrypt_file on disk; refuses to overwrite | ACCEPT, then REJECT overwrite | PASS |
