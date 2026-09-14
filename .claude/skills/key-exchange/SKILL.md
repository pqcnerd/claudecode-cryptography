---
name: key-exchange
description: Design authenticated key exchange / ECDH / Noise-style patterns with binding and confirmation.
when_to_use: Use for shared secret establishment. Examples: 'ECDH handshake', 'Noise pattern', 'derive session keys from DH'.
---

# key-exchange

## Inputs
- Parties, identities, mutual auth needs, FS requirements

## Procedure
1. Choose primitive (X25519, P-256 ECDH, KEM hybrid if PQ).
2. Specify authentication (signatures, pre-shared, Noise pattern).
3. Transcript: what enters the hash/KDF (identities, public keys, probs, versions).
4. KDF session keys with domain separation; separate directions/purposes.
5. Key confirmation if required.
6. Check UKS, replay, reflection, downgrade on version/cipher negotiation.
7. Ephemeral vs static roles; FS implications.

## Required output
```
Pattern:
DH/KEM:
Transcript fields:
KDF schedule:
Auth / confirmation:
Attacks considered:
```

## Failure conditions
- Raw shared secret used as key without KDF
- Unauthenticated cipher suite negotiation
- Missing identity binding in transcript

## Verification
Protocol-review + negative tests on transcript field omission.
