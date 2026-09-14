---
name: crypto-spec-conformance
description: Maintain SPEC SECTION → CODE → TEST mapping for cryptographic algorithms.
when_to_use: Use for Mode B standard/paper implementations and spec audits. Examples: 'spec map', 'conformance matrix', 'RFC section coverage'.
---

# crypto-spec-conformance

## Procedure
1. List normative sections affecting behavior.
2. For each: code location + test covering it.
3. Mark gaps as blocking for completion.
4. Include constants, DST labels, rejection rules.

## Required output
| Spec section | Code | Test | Status |

## Failure conditions
Magic constants without section citations.
