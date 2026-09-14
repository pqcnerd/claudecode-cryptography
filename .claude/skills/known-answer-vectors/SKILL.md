---
name: known-answer-vectors
description: Locate and apply official cryptographic known-answer test vectors.
when_to_use: Use when implementing standards or verifying correctness. Examples: 'RFC test vectors', 'NIST KAT', 'Wycheproof'.
---

# known-answer-vectors

## Procedure
1. Identify vector sources: RFC appendices, NIST CAVP/KAT, CFRG, Project Wycheproof, reference impl.
2. Prefer vendored fixtures under `evals/crypto/fixtures/` when present.
3. Map each vector to a unit test name.
4. Include encoding details (hex/base64, endianness).
5. Run and record pass/fail evidence.

## Required output
Vector source table + commands + results.

## Shell recipes
- `openssl dgst/enc/pkey` for some KATs when applicable
- Python `cryptography` / `nacl` as oracles for differential checks
- Compare hex outputs exactly

## Failure conditions
Inventing vectors; ignoring official ones that exist.
