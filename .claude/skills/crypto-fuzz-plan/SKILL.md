---
name: crypto-fuzz-plan
description: Plan fuzzing for cryptographic parsers and verification boundaries.
when_to_use: Use for parsers of keys, ciphertexts, proofs, ASN.1/DER, and verifiers. Examples: 'fuzz signature parser', 'cargo fuzz crypto'.
---

# crypto-fuzz-plan

## Procedure
1. Identify parse/verify entry points.
2. Prefer libFuzzer/cargo-fuzz/AFL++ when language fits.
3. Seeds from valid KATs; mutations for tags, lengths, points.
4. Assert no panics; reject invalid; never accept forged under key.
5. Bound corpus and timeouts.

## Required output
Targets, harness sketch, seeds, success criteria.

## Failure conditions
Fuzzing encrypt() with random plaintext only (low value) while ignoring parsers.
