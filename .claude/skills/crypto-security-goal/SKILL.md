---
name: crypto-security-goal
description: Clarify cryptographic security goals and required properties before selecting constructions.
when_to_use: Use when starting crypto design. Examples: 'what properties do we need', 'confidentiality vs authenticity', 'forward secrecy required?'.
---

# crypto-security-goal

## Inputs
- System description and assets
- Stated user requirements

## Questions
1. What asset must be protected (keys, messages, passwords, identities, ledgers)?
2. Against whom (network attacker, malicious server, compromised device, quantum adversary)?
3. Required properties: confidentiality, integrity, authenticity, FS, PCS, non-repudiation, anonymity/hiding, binding, unforgeability, replay resistance, downgrade resistance?
4. Is this primitive, construction, protocol, or application level?

## Procedure
1. Write one-sentence security goal.
2. List required properties with short why.
3. List explicitly non-goals.
4. Note lifetime and compromise boundaries (long-term keys vs session keys).
5. Hand off to `crypto-threat-model` then construction selection.

## Required output
```
Goal:
Assets:
Properties required:
Non-goals:
Compromise boundaries:
```

## Failure conditions
- Selecting AES-GCM (or any construction) before stating goal
- Mixing password-hashing goals with general hashing

## Verification
Properties list is non-empty and matched by later construction choice.
