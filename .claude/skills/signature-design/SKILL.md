---
name: signature-design
description: Design digital signature usage: scheme choice, domain separation, malleability, and verification.
when_to_use: Use when signing or verifying messages/artifacts. Examples: 'sign plugin manifests', 'Ed25519 vs ECDSA', 'domain separated signatures'.
---

# signature-design

## Inputs
- Message type; identity binding needs; malleability tolerance; curve constraints

## Procedure
1. Prefer Ed25519/EdDSA or well-bound ECDSA/Schnorr APIs; RSA-PSS over PKCS#1 v1.5 for new RSA.
2. Bind context: domain separation string, version, chain-id / intent (e.g. EIP-712).
3. Specify encoding of signed payload (canonical).
4. Verification: reject non-canonical encodings where required; define error behavior.
5. Note malleability (ECDSA/Schnorr) if consensus-critical.
6. Deterministic nonces for ECDSA (RFC 6979) when implementing Mode B.
7. Key lifecycle and revocation/rotation story.

## Required output
```
Scheme:
Signed payload format:
Domain separation:
Verification rules:
Malleability notes:
```

## Failure conditions
- Signing ambiguous serialization
- Missing identity/intent binding
- ECDSA with weak/repeated k (Mode B)

## Verification
Altered message fails; altered context fails; vectors if implementing.
