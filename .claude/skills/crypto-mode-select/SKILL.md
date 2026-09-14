---
name: crypto-mode-select
description: Classify cryptographic task mode: A production, B implementation/research, Audit, or Protocol.
when_to_use: Use at the start of any cryptography task before designing or coding. Examples: 'what mode is this', 'should I use a library', 'implement from RFC', 'review this crypto'.
---

# crypto-mode-select

## Inputs
- User task statement
- Whether existing code/library constraints exist
- Whether a paper/RFC/standard is named

## Questions to answer
1. Is the deliverable an application feature using crypto, or a crypto artifact itself?
2. Is the user asking to implement a primitive/construction/protocol from spec/paper?
3. Is the primary goal review/audit rather than greenfield implementation?
4. Is the core problem a multi-party handshake/state machine?

## Procedure
1. Map task → one primary mode: **A**, **B**, **Audit**, or **Protocol** (secondary tags allowed).
2. Mode **A** if: encrypting app data, tokens at rest, TLS client usage, password verify in product, calling AEAD/KDF APIs.
3. Mode **B** if: implement RFC/NIST/paper; field/curve/NTT/poly math; ZK/PQC/FHE/MPC engines; optimize crypto; educational reimplementation; cryptographic library development.
4. Mode **Audit** if: review, find bugs, threat-model existing code, compare to spec without owning the rewrite yet.
5. Mode **Protocol** if: design/review message flows, transcripts, downgrade/replay, handshake state.
6. State mode explicitly. List implications (library preference vs spec-driven impl).
7. Choose next skills (threat-model, api-choice, spec-research, protocol-review, etc.).

## Required output
```
Mode: A|B|Audit|Protocol
Rationale: ...
Next skills: ...
Forbidden shortcuts: ...
```

## Failure conditions
- Defaulting to "never implement crypto" on Mode B tasks
- Jumping to code before mode classification
- Treating audit-only requests as rewrite mandates

## Verification
Mode is stated before first code edit on crypto tasks.
