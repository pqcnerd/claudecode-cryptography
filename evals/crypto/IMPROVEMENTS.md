# Milestone 11 — Improvements from static eval / design review

Live dual-agent transcripts are still pending (`RESULTS.md` live log). This milestone closes **structural gaps** found while building the suite and fixture oracles.

## Failure / gap → patch

| Gap | Owning artifact | Patch |
|-----|-----------------|-------|
| AEAD decrypt ordering not explicit enough | `aead-design`, `crypto-audit` | Emphasize no plaintext before tag verify |
| Unauthenticated CBC not named in audit prompt | `crypto-audit` | Add to hunt list |
| CT language caveats easy to skip | `constant-time-review/reference.md` | Short per-language reference |
| Held-out overfitting risk | `TASKS/heldout_01_key_reuse.md` | New held-out task |
| Mode B library-nag risk | `crypto-mode-select`, `crypto-engineer` | Already present; add regression note in RESULTS |
| Fixture graders cover 4/8+ broken samples | `grade_fixture.py` | Document manual expected_findings for md fixtures |
| Expert packs might not auto-route | `crypto-engineer` | Keyword → pack table tightened |

## Patches applied

See git-visible updates in this milestone to agents/skills/rules/tasks.

## Re-score protocol

After live runs: re-grade adversarial fixtures ADV-01..08; require crypto agent hit rate ≥ 80% on `expected_findings` before calling specialization done.
