---
name: crypto-threat-model
description: Build a concise cryptographic threat model: assets, adversaries, trust and compromise boundaries.
when_to_use: Use before designing crypto or auditing. Examples: 'threat model this', 'who is the adversary', 'what if the server is breached'.
---

# crypto-threat-model

## Inputs
- Security goal output
- Deployment context (client/server/HSM/browser/chain)

## Questions
1. Who are the adversaries (Dolev–Yao network, malicious endpoint, insider, quantum)?
2. What can they read, modify, replay, or choose?
3. What is trusted (HSM, KMS, OS RNG, CA store, enclave)?
4. What happens on key compromise / nonce-state loss / clock skew?

## Procedure
1. List assets and trust anchors.
2. List adversary capabilities.
3. Identify compromise boundaries (KEK vs DEK, long-term vs ephemeral).
4. Enumerate relevant attacks: eavesdrop, tamper, replay, downgrade, oracle, nonce reuse, cross-protocol, UKS, invalid curve, timing.
5. Map each required property to an adversary limitation.
6. Note out-of-scope threats.

## Required output
```
Assets:
Adversaries:
Trust anchors:
Compromise boundaries:
In-scope attacks:
Out of scope:
```

## Failure conditions
- Handwavy "secure against hackers"
- Ignoring state loss (nonce counters) or backup/restore cloning of RNG/state

## Verification
Every chosen construction later cites which threat it addresses.
