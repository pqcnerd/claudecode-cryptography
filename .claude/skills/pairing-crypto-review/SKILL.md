---
name: pairing-crypto-review
description: Review pairing-based crypto: BLS12-381/BN254, G1/G2, BLS, pairing assumptions.
when_to_use: Use for pairings, BLS signatures, BN254/alt_bn128, BLS12-381, pairing-based proofs. Examples: 'BLS verify', 'G1 G2', 'pairing check'.
---

# pairing-crypto-review

## Procedure
1. Identify curve (BLS12-381, BN254) and groups G1/G2/GT.
2. Subgroup checks and hashing-to-curve per spec.
3. Pairing product equations for the scheme (BLS, KZG verify, etc.).
4. Serialization of points/field elements; conjugation/coeff order.
5. Domain separation for hash-to-curve / messages.
6. Performance vs safety tradeoffs; do not skip subgroup checks silently.

## Required output
Curve, equations, validation, domain sep, SPEC→CODE→TEST stubs.
