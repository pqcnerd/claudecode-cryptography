---
name: side-channel-review
description: Adversarial side-channel review: timing, cache, logs, errors, and speculative concerns.
when_to_use: Use for low-level crypto or when auditing for leakage. Examples: 'side channel review', 'cache timing', 'secrets in logs'.
---

# side-channel-review

## Inputs
- Implementation; deployment (shared CPU, browser, enclave)

## Procedure
1. Run constant-time checklist on secret paths.
2. Check logs, exceptions, metrics, debug formatters for secret bytes.
3. Error oracle: distinct errors for padding vs MAC vs cert?
4. Table lookups / S-boxes indexed by secret.
5. Speculative execution notes only when relevant to threat model.
6. Allocations that retain secrets; swap; core dumps.
7. Recommend mitigations or API changes; do not invent false guarantees.

## Required output
Finding blocks:
```
SEVERITY:
LOCATION:
CRYPTOGRAPHIC ISSUE:
WHY IT MATTERS:
ATTACK / FAILURE MODEL:
RECOMMENDED FIX:
VERIFICATION:
```

## Failure conditions
- Ignoring log leakage because "timing looks fine"
- Absolute CT claims

## Verification
Spawn `sidechannel-review` agent for formal pass on large changes.
