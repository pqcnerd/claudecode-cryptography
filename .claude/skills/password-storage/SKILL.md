---
name: password-storage
description: Design password hashing and verification with Argon2/scrypt and safe APIs.
when_to_use: Use for login password storage or passphrase-based keys. Examples: 'hash passwords', 'store user credentials', 'derive key from passphrase'.
---

# password-storage

## Inputs
- Online vs offline threat; UX latency budget; KDF-for-key vs password-verify

## Procedure
1. Forbid SHA-*/MD5/SHA1(password) and unsalted hashes.
2. Prefer Argon2id for password verification; scrypt acceptable; PBKDF2 only for compatibility.
3. Unique random salt per password (≥128 bits).
4. Tune memory/time/parallelism to threat; document parameters.
5. Constant-time compare of stored verifier (or use API that does).
6. For passphrase→key: use dedicated KDF; then AEAD; never reuse password hash as AEAD key without KDF structure.
7. Plan migration/rehash on login when parameters change.

## Required output
```
Scheme:
Parameters:
Salt:
Verify API:
Migration:
```

## Failure conditions
- SHA256(password)
- Global static salt
- Leaking whether username exists via distinct crypto errors (product policy aside)

## Verification
Wrong password fails; parameter upgrade path tested.
