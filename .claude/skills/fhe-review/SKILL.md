---
name: fhe-review
description: Review FHE engineering: BFV/BGV/CKKS/TFHE, noise, keys, bootstrapping tradeoffs.
when_to_use: Use for fully/somewhat homomorphic encryption work. Examples: 'CKKS', 'TFHE', 'bootstrapping', 'relinearization', 'BFV'.
---

# fhe-review

## Procedure
1. Scheme and approx vs exact arithmetic needs (CKKS vs BFV/BGV/TFHE).
2. Parameter selection vs noise budget.
3. Key material: secret, evaluation, switching, relinearization keys — protect eval keys appropriately.
4. Encoding/plaintext modulus; rescale; bootstrapping necessity.
5. Side-channel and key-management for long-lived FHE keys.
6. Correctness tests including noise-induced failures.

## Required output
Scheme, params rationale, key hierarchy, noise/testing plan.
