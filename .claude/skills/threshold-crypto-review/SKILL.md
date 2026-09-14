---
name: threshold-crypto-review
description: Review threshold crypto and MPC: secret sharing, DKG, threshold signatures, threat models.
when_to_use: Use for threshold signatures, Shamir sharing, DKG, MPC keygen. Examples: 'threshold ECDSA', 'DKG', 'Shamir', 'share refresh'.
---

# threshold-crypto-review

## Procedure
1. Threat model: semi-honest vs malicious; dishonest majority assumptions.
2. Share lifecycle: gen, distribute, store, use, refresh, revoke.
3. DKG transcript and complaints; identifiable aborts if claimed.
4. Threshold signatures: partial sig validation; aggregation binding.
5. Key refresh / proactive security.
6. Network adversary: replay of rounds; transcript binding.

## Required output
Assumptions, threshold params, share lifecycle, protocol risks.
