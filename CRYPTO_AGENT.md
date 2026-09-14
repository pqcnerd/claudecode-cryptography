# Cryptography Coding Agent

This Claude Code tree is specialized for **cryptographic software engineering**.

## Quick start

Project defaults (already set):

```json
// .claude/settings.json
{
  "agent": "crypto-engineer",
  "outputStyle": "cryptography"
}
```

Or:

```bash
claude --agent crypto-engineer
```

Bundled skill (always registered): `/crypto-mode`

Opt out of the built-in crypto agent fallback: `CLAUDE_CODE_DISABLE_CRYPTO_ENGINEER=1`

## What you get

| Layer | Location |
|-------|----------|
| Main orchestrator | `.claude/agents/crypto-engineer.md` (+ built-in fallback) |
| Review agents | `crypto-audit`, `crypto-verify`, `sidechannel-review`, `crypto-spec-review` |
| Domain agents | `crypto-ecc`, `crypto-zk`, `crypto-lattice` |
| Procedural skills | `.claude/skills/*/SKILL.md` |
| Rules / memory | `CLAUDE.md`, `.claude/rules/` |
| Output style | `.claude/output-styles/cryptography.md` |
| Architecture | `.claude/ARCHITECTURE.md` |
| Evals | `evals/crypto/` |

## Modes

- **A — Production:** Prefer audited libraries; do not invent primitives.
- **B — Implementation/research:** Implementing standards/papers/arithmetic is expected; strict verification.
- **Audit / Protocol:** Review- and transcript-first.

## Will / won't

**Will:** design/implement/review cryptography, reason about how constructions fail for defense and audit, demand KATs and adversarial review.

**Won't:** silently invent product crypto; claim constant-time in managed languages without caveats; treat round-trip tests as security proofs; rewrite global cyber-risk policy.

## Evals

See [`evals/crypto/README.md`](evals/crypto/README.md), [`RUBRIC.md`](evals/crypto/RUBRIC.md), [`RESULTS.md`](evals/crypto/RESULTS.md).
