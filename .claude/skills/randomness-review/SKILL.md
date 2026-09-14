---
name: randomness-review
description: Review CSPRNG usage, entropy, bias, fork/VM cloning, and deterministic generation.
when_to_use: Use when generating keys, nonces, salts, or scalars. Examples: 'is our RNG safe', 'modulo bias', 'fork safety'.
---

# randomness-review

## Inputs
- RNG API in use; deterministic vs OS entropy; virtualization/forking

## Procedure
1. Require CSPRNG (OS getrandom/SecureRandom/crypto.randomBytes)—not Math.random / glibc rand.
2. Check bias: rejection sampling vs naive mod p for scalars.
3. Nonce generation strategy interaction with RNG failure.
4. Fork/VM snapshot cloning: danger of RNG state duplication.
5. DRBG seeding and reseed policies if custom.
6. Failure handling when RNG fails (abort, don't silently fall back).

## Required output
```
RNG API:
Bias analysis:
Fork/clone risks:
Failure behavior:
```

## Failure conditions
- Unseeded PRNG for keys
- `secret = random() % p` without rejection
- Continuing after RNG error

## Verification
Tests mock RNG failure; statistical/unit checks for rejection sampler if Mode B.
