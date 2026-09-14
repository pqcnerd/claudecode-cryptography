---
name: crypto-code-review
description: Structured review checklist for cryptographic code changes.
when_to_use: Use when reviewing a crypto diff or PR. Examples: 'review this crypto PR', 'checklist for cipher change'.
---

# crypto-code-review

## Procedure
1. Identify mode (A/B/Audit/Protocol) and construction.
2. Check spec citations and parameter match.
3. Key/nonce/domain separation/serialization.
4. Auth ordering and failure behavior.
5. Secret vs public; CT notes.
6. Tests: KAT, negative, property.
7. Spawn specialists if needed (audit/verify/sidechannel/spec).

## Required output
Summary + list of blocking vs non-blocking issues using the standard finding schema.

## Failure conditions
- Style-only review without crypto properties
- Approving without tests on crypto changes

## Verification
Blocking issues resolved or explicitly accepted with rationale.
