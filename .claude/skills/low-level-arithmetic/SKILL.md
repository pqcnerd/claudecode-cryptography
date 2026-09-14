---
name: low-level-arithmetic
description: Implement and review field/bigint limb arithmetic, Montgomery/Barrett, canonical encoding, rejection sampling.
when_to_use: Use for Mode B arithmetic: Montgomery mul, field elements, scalars, NTT helpers, big-int crypto math. Examples: 'Montgomery multiplication', 'canonical field encoding', 'rejection sampling scalars'.
---

# low-level-arithmetic

## Inputs
- Field/modulus; limb width; target language; const-time requirements

## Procedure
1. Document mathematical representation vs code representation (symbols → variables).
2. Specify limb size, endianness, saturated vs unsaturated, carry strategy.
3. Modular reduction: Montgomery / Barrett / specialized; prove bounds.
4. Inversion: Fermat vs CT methods; batch inversion when useful.
5. Canonical encoding: unique byte representation; reject non-canonical at parse.
6. Scalar reduction and rejection sampling (no naive mod bias).
7. Separate **mathematically correct** from **cryptographically safe** (CT, validation).
8. Temporary buffers: ownership, zeroization limits.

## Required output
```
Representation:
Ops:
Encoding:
Validation/rejection:
CT considerations:
SPEC→CODE map:
```

## Failure conditions
- Non-canonical accepted as unique
- Biased scalar generation
- Secret-dependent early exit in reduction

## Verification
KATs; boundary values; fuzz parse/canonicalize.
