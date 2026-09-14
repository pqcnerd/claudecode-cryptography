---
name: nonce-iv-review
description: Review nonce/IV/counter uniqueness, persistence, overflow, and misuse consequences.
when_to_use: Use for any AEAD/stream cipher or IV-using mode. Examples: 'GCM nonce', 'counter overflow', 'random vs sequential nonce'.
---

# nonce-iv-review

## Inputs
- Algorithm nonce requirements; multi-writer; durable state

## Procedure
1. State uniqueness requirement (per-key for GCM/ChaCha20-Poly1305).
2. Choose random (enough bits: e.g. 96-bit GCM careful; prefer 192-bit XChaCha) vs counter.
3. Counter: persistence, atomic allocation, overflow → key retire.
4. Multi-writer: partition nonce space or use misuse-resistant AEAD (GCM-SIV/AES-GCM-SIV) / XChaCha random.
5. IV for CBC legacy: unpredictable; still not authenticated alone.
6. Document misuse consequences (GCM forgery after nonce reuse).

## Required output
```
Algorithm:
Nonce length:
Generation:
Persistence/overflow:
Misuse impact:
```

## Failure conditions
- Key||message-count without overflow plan
- Random 64-bit nonces for high volume GCM
- Reusing IV with same key intentionally "for testing" in production paths

## Verification
Tests that detect duplicate nonces under concurrency where applicable.
