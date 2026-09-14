---
name: blockchain-crypto-review
description: Review blockchain cryptography: signatures, Merkle proofs, EIP-712, VRF, aggregators, verifiers.
when_to_use: Use for chain crypto. Examples: 'EIP-712', 'Merkle proof', 'secp256k1', 'BLS aggregate', 'commit-reveal', 'VRF'.
---

# blockchain-crypto-review

## Procedure
1. Identify primitive (ECDSA/Schnorr/BLS) and domain separation (chain id, intent).
2. EIP-712 / typed data: types hash correctly; phishing via type confusion.
3. Merkle/MPT proofs: inclusion vs exclusion; hash function domain sep.
4. Aggregates/thresholds: rogue-key and proof-of-possession.
5. Commit-reveal timing; VRF verification.
6. Smart-contract verifier: precompiles, gas, malleability for consensus.

## Required output
Scheme, domain binding, verifier checklist, findings.
