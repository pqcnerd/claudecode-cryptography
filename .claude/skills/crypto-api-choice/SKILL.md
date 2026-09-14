---
name: crypto-api-choice
description: Select production cryptographic libraries and APIs (Mode A) matched to the security goal.
when_to_use: Use for application/production crypto. Examples: 'which library', 'libsodium vs WebCrypto', 'how should we encrypt tokens'.
---

# crypto-api-choice

## Inputs
- Mode must be A (or hybrid with clear A boundary)
- Language/platform constraints

## Procedure
1. Confirm Mode A. If Mode B, stop and use `crypto-spec-research` instead.
2. Map goal → construction (AEAD, sig, KEX, KEM, password KDF, HKDF).
3. Prefer maintained audited APIs:
   - libsodium / Sodium
   - RustCrypto / ring / aws-lc-rs
   - BoringSSL / OpenSSL (careful API misuse)
   - WebCrypto
   - Tink / high-level misuse-resistant APIs
   - Established TLS/Noise libraries
4. Reject homemade AES-ECB, unauthenticated CBC, raw RSA, SHA(password).
5. Document versioning, algorithm agility policy, and misuse footguns of chosen API.
6. Define key sizes and algorithm identifiers.

## Required output
```
Construction:
Library/API:
Why:
Rejected alternatives:
Misuse footguns to avoid:
```

## Failure conditions
- Inventing a primitive for product code
- Picking low-level OpenSSL EVP without misuse review

## Verification
Choice provides authenticity if confidentiality is required (AEAD or encrypt-then-MAC with proof of composition).
