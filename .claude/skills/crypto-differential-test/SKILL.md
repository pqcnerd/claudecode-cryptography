---
name: crypto-differential-test
description: Compare implementation against an established cryptographic oracle/reference.
when_to_use: Use when another implementation exists. Examples: 'compare to openssl', 'differential test HKDF', 'match libsodium'.
---

# crypto-differential-test

## Procedure
1. Choose oracle (OpenSSL, libsodium, BoringSSL, ref code).
2. Shared inputs: keys, messages, nonces, domain sep.
3. Compare outputs bit-exactly (or per spec allowable representations).
4. Mutate inputs and compare rejection behavior.
5. Document version of oracle.

## Required output
Oracle, input set, mismatches, commands.

## Failure conditions
Comparing only success paths; ignoring error behavior differences that are security-relevant.
