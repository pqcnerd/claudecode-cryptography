---
name: crypto-test-plan
description: Create a cryptographic test plan: KAT, negative, property, differential, fuzz, fault.
when_to_use: Use before or while implementing crypto. Examples: 'test plan for AEAD', 'how to test HKDF', 'crypto tests'.
---

# crypto-test-plan

## Procedure
Define tests in these categories (skip only with rationale):
1. **Known-answer** — official vectors
2. **Negative** — wrong key/nonce/tag/AAD; malformed; truncated; oversized
3. **Property** — round-trip; verify fails on mutation; canonical uniqueness
4. **Differential** — vs OpenSSL/libsodium/ref
5. **Fuzz** — parsers and verifiers
6. **Fault** — RNG fail; nonce state loss; counter limit; auth fail paths

## Required output
```
KAT:
Negative:
Property:
Differential:
Fuzz:
Fault:
Commands:
```

## Failure conditions
Only encrypt/decrypt assert equal.
