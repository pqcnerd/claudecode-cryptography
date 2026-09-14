# Running crypto agent evals

## Manual protocol

1. Pick a task file from `evals/crypto/TASKS/`.
2. **Baseline run:** start Claude Code without project crypto agent if comparing defaults, or temporarily set `"agent"` aside; use general-purpose behavior. Save transcript to `evals/crypto/runs/<task-id>-baseline.md`.
3. **Crypto run:** ensure `.claude/settings.json` has `agent: crypto-engineer` (or `--agent crypto-engineer`). Save to `evals/crypto/runs/<task-id>-crypto.md`.
4. Grade both with `../RUBRIC.md` and the task's `expected_findings`.
5. For fixtures under `../fixtures/`, run `python3 grade_fixture.py <fixture>` when available.

## Preferred evidence

- Commands executed and outputs
- Whether Mode A/B was stated
- Whether subagents/skills were used
- Fixture oracle results
