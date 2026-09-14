---
name: lattice-crypto-review
description: Review lattice/PQC crypto: ML-KEM/ML-DSA/Falcon, NTT, noise, sampling, CT concerns.
when_to_use: Use for PQC and lattices. Examples: 'Kyber', 'ML-KEM', 'Dilithium', 'ML-DSA', 'Falcon', 'NTT', 'LWE', 'rejection sampling'.
---

# lattice-crypto-review

## Procedure
1. Identify scheme and parameter set (NIST names).
2. Polynomial ring, modulus, NTT roots — must match spec exactly.
3. Sampling: CBD/Gaussian/rejection; bias and CT.
4. Noise growth / decryption failure rates (awareness).
5. Encoding of keys/ciphertexts/signatures; bounds checks.
6. Side-channel: secret-dependent rejection, table access.
7. Mode A: vetted PQC libs; Mode B: vectors + differential vs reference.

## Required output
Scheme/params, NTT/sampling notes, CT risks, vector plan.
