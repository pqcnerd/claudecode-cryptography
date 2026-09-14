---
name: hash-mac-kdf
description: Choose and design hashing, MACs, and KDFs including HKDF and password KDFs.
when_to_use: Use for integrity, PRFs, key derivation, or hashing design. Examples: 'HKDF for handshake', 'HMAC vs hash', 'derive session keys'.
---

# hash-mac-kdf

## Inputs
- Purpose: collision-resistant hash vs MAC vs KDF vs password hashing

## Procedure
1. Classify need:
   - Hash (SHA-2/SHA-3/BLAKE2/BLAKE3) for fingerprints/commits—not for passwords
   - MAC (HMAC, KMAC, Poly1305-as-part-of-AEAD) for authenticity with key
   - KDF (HKDF extract-then-expand) for deriving keys from key material
   - Password KDF (Argon2id preferred; scrypt; PBKDF2 only for compatibility)
2. For HKDF: specify Hash, salt, IKM, info/context (bind protocol, version, parties).
3. Never use raw SHA as KDF without extract/expand story.
4. Domain-separate labels for each derived key purpose.
5. Document output lengths.

## Required output
```
Purpose classification:
Algorithm:
Parameters (salt/info/context):
Derived key schedule:
```

## Failure conditions
- SHA256(password) for password storage
- HKDF with empty/meaningless info when contexts differ
- Using hash(tag||msg) as MAC without justification

## Verification
Known-answer vectors for HKDF/HMAC when implementing; context binding tests.
