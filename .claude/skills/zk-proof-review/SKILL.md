---
name: zk-proof-review
description: Review ZK proof systems: arithmetization, PCS, Fiat-Shamir, public inputs, verifier boundaries.
when_to_use: Use for zero-knowledge proofs. Examples: 'Groth16', 'PLONK', 'STARK', 'Fiat-Shamir', 'KZG', 'R1CS', 'public inputs'.
---

# zk-proof-review

## Procedure
1. Identify proof system and arithmetization (R1CS, PLONK-ish, AIR).
2. Public inputs vs witness; binding in verifier.
3. Polynomial commitment (KZG/FRI/…) and trusted setup assumptions if any.
4. Fiat–Shamir transcript: domain separation, all statements absorbed.
5. Serialization of proofs; malleability; verification equation completeness.
6. Soundness vs completeness bugs; under-constrained circuits (if circuit review).
7. On-chain verifier integration pitfalls (field modulus, gas, calldata encoding).

## Required output
System, transcript bind list, public-input checklist, findings.
