---
name: serialization-review
description: Review cryptographic serialization, canonicalization, framing, and ambiguous concatenation.
when_to_use: Use when encoding keys, ciphertexts, transcripts, proofs, or signed payloads. Examples: 'canonical encoding', 'length prefix', 'DER issues'.
---

# serialization-review

## Inputs
- Formats; parsers; versioning needs

## Procedure
1. Require unambiguous framing (length prefixes / fixed widths / ASN.1 carefully).
2. Canonical field/element/point encodings; compressed points rules.
3. Reject non-canonical where uniqueness required.
4. Version bytes and type tags to prevent confusion.
5. DER vs BER pitfalls; trailing data rejection.
6. Endianness consistency with spec.
7. Fuzz parser boundaries.

## Required output
```
Format:
Canonical rules:
Rejection rules:
Ambiguity analysis:
Fuzz plan:
```

## Failure conditions
- `hash(a||b)` with variable-length a,b and no separator
- Accepting multiple encodings of same point as distinct or vice versa incorrectly

## Verification
Round-trip + non-canonical reject tests + fuzz.
