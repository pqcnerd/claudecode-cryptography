# Cryptography Coding Agent — Architecture

This project specializes Claude Code as a **cryptography software engineer** first, general programmer second.

## Delivery strategy

1. Project-level specialization under `.claude/` + root `CLAUDE.md` + `evals/crypto/`
2. Optional promotion to bundled skills / built-in agents only after evals prove lift
3. Do **not** rewrite `constants/prompts.ts` or edit `constants/cyberRiskInstruction.ts`

## Activation

```json
// .claude/settings.json
{ "agent": "crypto-engineer", "outputStyle": "cryptography" }
```

Or: `claude --agent crypto-engineer`

## Mode classification (required on every crypto task)

| Mode | When | Behavior |
|------|------|----------|
| **A — Production / application** | App features, storage, TLS clients, product KDF/MAC | Prefer audited libraries; discourage inventing primitives |
| **B — Implementation / research** | Libraries, RFCs, papers, field/curve/NTT/ZK/PQC/FHE | Implementing primitives is expected; strict spec→vectors→CT workflow; do not nag "use a library" |
| **Audit** | Review existing crypto | Prefer crypto-audit, crypto-spec-review, sidechannel-review |
| **Protocol** | Handshake / state machine | Transcript-first; protocol-review skill |

## Decision ladder

1. Security goal → 2. Threat model → 3. Mode → 4. Spec hierarchy → 5. Properties → 6. Construction → 7. Library (A) or representation (B) → 8. Key lifecycle → 9. Nonce/IV → 10. Domain separation → 11. Serialization → 12. Transcript binding → 13. Replay/downgrade/malleability → 14. Secret-dependent control/memory → 15. Implement → 16. KATs → 17. Negative tests → 18. Property tests → 19. Differential tests → 20. Fuzz parsers → 21. Adversarial review → 22. Side-channel review → 23. Spec conformance → 24. Complete

## Spec source hierarchy

1. Governing protocol/spec → 2. RFC/IETF/CFRG → 3. NIST/FIPS → 4. Official library docs → 5. Reference implementation → 6. Original paper → 7. Reputable literature → 8. Secondary explainers (supporting only)

## Responsibility split

- **crypto-engineer** — main orchestrator; classifies mode; runs ladder; spawns specialists
- **Skills** — procedural playbooks (~80–180 lines); not textbooks; optional `reference.md`
- **Review subagents** — crypto-audit, crypto-verify, sidechannel-review, crypto-spec-review
- **Expert packs** — ECC, pairings, ZK, lattice/PQC, threshold/MPC, FHE, blockchain (on demand)

## Skill frontmatter template

```yaml
---
name: skill-id
description: One-line purpose
when_to_use: When to invoke. Examples: '...'
---
```

Optional: `paths`, `allowed-tools`, `context: fork`, `agent`

## Agent frontmatter (loader-faithful)

Required: `name`, `description`. Optional: `tools`, `disallowedTools`, `skills`, `mcpServers`, `model`, `effort`, `permissionMode`, `memory`, `color`, `maxTurns`, `background`, `isolation`, `initialPrompt`

## Subagent tool policy

Review agents deny Write/Edit/NotebookEdit/Agent by default (verification-style). crypto-verify allows Bash for tests; tmp scripts OK.

## Eval philosophy

Compare default agent vs crypto-engineer on identical tasks. Prefer executable fixtures, KATs, and expected-finding keys over prose grading alone. See `evals/crypto/`.

## MCP

Prefer shell recipes + vendored vectors. Add `.mcp.json` only when an eval demonstrates lift. Deferred by default until Milestone 9 justification.


## Milestone 9 tooling decision

MCP is **deferred**. Skills document shell oracles instead:

- OpenSSL CLI when available
- Python stdlib `hashlib` / optional `cryptography` for differential checks
- Vendored fixtures + `evals/crypto/harness/grade_fixture.py`
- WebFetch for RFC/NIST retrieval during agent sessions

Add `.mcp.json` only after an eval shows MCP-specific lift.

## Milestone 12 productization

- Bundled skill: `/crypto-mode` via `skills/bundled/cryptoMode.ts`
- Built-in agent fallback: `tools/AgentTool/built-in/cryptoEngineerAgent.ts` (opt out `CLAUDE_CODE_DISABLE_CRYPTO_ENGINEER=1`)
- Docs: `CRYPTO_AGENT.md`
- Source of truth for deep procedures remains `.claude/skills/` and `.claude/agents/`
