---
name: crypto-spec-research
description: Locate and extract governing cryptographic specifications, parameters, encodings, and test vectors.
when_to_use: Use when implementing or reviewing standards/RFCs/NIST/papers. Examples: 'implement RFC 5869', 'what does NIST say', 'find test vectors'.
---

# crypto-spec-research

## Inputs
- Algorithm/protocol name
- Mode (prefer B or Audit when specs bind)

## Spec hierarchy
1. Governing protocol spec
2. RFC / IETF / CFRG
3. NIST / FIPS
4. Official library docs
5. Reference implementation
6. Original paper
7. Literature
8. Secondary blogs (supporting only)

## Procedure
1. Identify canonical document IDs (RFC number, FIPS, paper).
2. Fetch/read authoritative sections for: parameters, encodings, domain separation, rejection rules, edge cases.
3. Extract parameter sizes, endianness, constants.
4. Locate official / reference test vectors.
5. Note deviations commonly found in stacks.
6. Produce SPEC SECTION → planned CODE → TEST mapping stubs.

## Required output
```
Primary spec:
Sections:
Parameters:
Encoding/endianness:
Domain separation / labels:
Rejection / validation rules:
Test vector sources:
SPEC→CODE→TEST stubs:
```

## Failure conditions
- Implementing from memory when a spec exists
- Using blog pseudocode as primary source

## Verification
Primary spec cited before Mode B implementation begins.
