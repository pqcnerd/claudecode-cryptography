---
name: aead-design
description: Design AEAD encryption: algorithm choice, keys, nonces, AAD, tags, and failure handling.
when_to_use: Use when encrypting data with authenticity. Examples: 'encrypt local secrets', 'AES-GCM design', 'XChaCha20-Poly1305'.
---

# aead-design

## Inputs
- Threat model; message size; uniqueness of nonces; multi-key needs

## Procedure
1. Prefer AEAD: AES-GCM, AES-GCM-SIV (nonce misuse), ChaCha20-Poly1305, XChaCha20-Poly1305 (large/random nonces).
2. Define key source and separation (no key reuse across algorithms/purposes).
3. Nonce strategy: random (sufficient length) vs counter (persistence, overflow, multi-writer).
4. Define AAD: bind identity, version, path, algorithm id—never leave context unbound if relevant.
5. Tag length and failure: **verify tag before any plaintext release** (no decrypt-then-deliver-then-check). Prefer uniform errors on auth failure.
6. Forbid ECB; forbid unauthenticated CBC for new designs.
7. Plan rotation and max messages per key.

## Required output
```
AEAD:
Key:
Nonce strategy:
AAD:
Tag/failure behavior:
Limits / rotation:
```

## Failure conditions
- Nonce reuse risk unaddressed for GCM/ChaCha20-Poly1305
- Decrypt-then-verify ordering
- Silent truncation of ciphertext/tag

## Verification
Negative tests: wrong key, wrong nonce, flipped ciphertext, flipped AAD, truncated tag.
