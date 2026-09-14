---
name: transcript-design
description: Design protocol transcripts and context binding for hashes, MACs, and signatures.
when_to_use: Use when defining what bytes enter hashes/KDFs/signatures in a protocol. Examples: 'Fiat-Shamir transcript', 'handshake transcript', 'context binding'.
---

# transcript-design

## Inputs
- Protocol messages; hash/KDF/sign APIs

## Procedure
1. List every field that must be bound (keys, nonces, identities, versions, alg ids, AD).
2. Define transcript encoding (length-prefixed, canonical).
3. Domain separation label for the protocol.
4. Specify when transcript is hashed vs MACed vs signed.
5. For Fiat–Shamir: bind statement, public inputs, proof elements per spec; no missing domain sep.
6. Negative tests: omit each critical field and ensure acceptance fails.

## Required output
```
Transcript diagram:
Encoding:
Labels:
Bind list:
Negative tests:
```

## Failure conditions
- Hashing only message payloads without identities/alg
- FS challenge from incomplete transcript

## Verification
Mutation tests on transcript fields.
