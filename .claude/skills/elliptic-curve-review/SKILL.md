---
name: elliptic-curve-review
description: Review or implement ECC: ECDSA/EdDSA/X25519, validation, cofactor, malleability, nonces.
when_to_use: Use for elliptic-curve cryptography. Examples: 'ECDSA review', 'Ed25519', 'X25519', 'secp256k1', 'P-256', 'cofactor', 'invalid curve'.
---

# elliptic-curve-review

## Procedure
1. Identify curve and scheme (ECDSA, EdDSA/Ed25519, ECDH/X25519, Schnorr).
2. Check public-key validation / point-on-curve / subgroup / cofactor handling.
3. Encoding: compressed points, non-canonical scalars/points.
4. ECDSA: deterministic k (RFC 6979) if implementing; never reuse k; hash prefixing.
5. Malleability implications if consensus-critical.
6. Constant-time scalar mul considerations (Mode B).
7. Mode A: prefer vetted libs; Mode B: SPEC→CODE→TEST + vectors.

## Required output
Curve/scheme, validation rules, nonce strategy, findings (schema if audit).

## Failure conditions
Missing PK validation; ECDSA k reuse; accepting invalid curve points.
