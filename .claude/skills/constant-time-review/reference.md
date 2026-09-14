# Constant-time / zeroization caveats (quick reference)

Read this when claiming constant-time behavior or secret wiping.

## C / C++
- Compilers may remove "dead" zeroization; use `memset_s`, `explicit_bzero`, or vetted wipe helpers.
- CT helpers (`crypto_verify_*`, `ConstantTimeSelect`) beat hand-rolled masks.
- `-O` can rewrite branches; validate with tooling when threat model requires.

## Rust
- `subtle` crate helps; LLVM may still surprise you — not a hard guarantee.
- `Zeroize` trait helps but cannot erase copies/moves you forgot.
- Avoid secret-indexed slices/tables.

## Go
- `subtle.ConstantTimeCompare` for compares; `big.Int` is not CT.
- Interfaces/GC make absolute CT claims weak.

## Java
- JIT makes reliable CT extremely hard; prefer high-level APIs; avoid claims.

## JavaScript / TypeScript
- Not a CT environment. Use typed-array best-effort compares only as defense-in-depth; do not advertise CT.

## Python
- Not CT. Prefer `hmac.compare_digest`; never claim CT for custom loops.

## Always
- Distinguish **intent** (written to avoid secret branches) from **guarantee** (proven under compiler/CPU model).
- Secrets in logs/exceptions beat most timing fixes in severity for many apps.
