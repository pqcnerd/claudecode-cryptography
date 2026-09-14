---
name: kem-design
description: Design KEM/DEM hybrid encryption and binding between encapsulation and AEAD.
when_to_use: Use for KEM-based encryption or PQ hybrid. Examples: 'ML-KEM hybrid', 'HPKE-style design', 'KEM then AEAD'.
---

# kem-design

## Inputs
- Target security (classical/PQ/hybrid); recipient keys; AEAD choice

## Procedure
1. Separate KEM (encapsulate shared secret) from DEM/AEAD (encrypt message).
2. Derive AEAD key via KDF binding: KEM ciphertext, recipient id, algorithm ids, context.
3. Prefer standardized hybrids / HPKE-like constructions when applicable.
4. Define encapsulation encoding and validation.
5. Failure: reject malformed encapsulations uniformly where possible.
6. Mode A: use vetted library. Mode B: follow spec + KATs.

## Required output
```
KEM:
DEM/AEAD:
KDF binding fields:
Encodings:
```

## Failure conditions
- Using KEM shared secret directly as AEAD key without KDF/context
- Omitting ciphertext/public-key binding (key-mismatch attacks)

## Verification
KATs; wrong recipient fails; tampered encapsulation fails.
