---
name: constant-time-review
description: Review code for secret-dependent branches, indices, and variable-time operations with language caveats.
when_to_use: Use on secret-handling crypto code. Examples: 'constant time compare', 'secret dependent branch', 'is this CT'.
---

# constant-time-review

## Inputs
- Code paths touching secrets; language/runtime

## Look for
- Branches on secrets
- Secret-dependent memory indices / table lookups
- Early-return compares (password, MAC)
- Variable-time bigint div/mod
- Secret-dependent loop counts
- Rejection paths that leak via timing

## Language caveats (always state)

Read `reference.md` beside this skill for details. Summary:
- C/C++: volatile tricks fragile; use vetted CT helpers; compiler can wreck intent
- Rust: still depends on LLVM; use subtle/`black_box` carefully; not a guarantee
- Go: runtime/GC; careful with big.Int
- Java: JIT; no reliable CT; prefer APIs designed for it
- JS/Python: essentially not CT; avoid claiming CT; use best-effort compare helpers only as defense-in-depth

## Procedure
1. Mark secret vs public.
2. Trace compares, selects, table access.
3. Check MAC/tag verify APIs.
4. Document residual risk honestly.

## Required output
```
Secret data:
Findings:
Language caveats:
Residual risk:
```

## Failure conditions
- Claiming "constant time" in JS/Python without heavy caveats
- Ignoring compiler/JIT

## Verification
Code review notes + optional dudect/ci timing tests where applicable (never overclaim).
