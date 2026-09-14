---
name: protocol-review
description: Review cryptographic protocols for replay, downgrade, binding, and state-machine flaws.
when_to_use: Use for handshakes and multi-message protocols. Examples: 'review protocol for replay', 'downgrade', 'UKS', 'handshake review'.
---

# protocol-review

## Inputs
- Message flow or code implementing it; threat model

## Procedure
1. List participants, identities, trust assumptions.
2. Draw message sequence:
   `A -> B: ...` / `B -> A: ...`
3. State machine: states, timeouts, retries, concurrency.
4. What is encrypted, MACed, signed, hashed into transcript.
5. Check: replay, reordering, reflection, UKS, downgrade, version negotiation, key confirmation, FS/PCS, cross-protocol, crash recovery, nonce/counter state.
6. Identity and channel binding.
7. Produce findings with attack sketches.

## Required output
```
Participants:
Message flow:
Transcript contents:
State machine notes:
Findings: (standard schema)
```

## Failure conditions
- Reviewing primitives only while ignoring transcript
- Missing unauthenticated version/cipher negotiation

## Verification
At least one adversarial scenario analyzed even if benign.
