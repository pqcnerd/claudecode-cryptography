# Cryptography Agent Evaluation Suite

Compares the **default general agent** vs **crypto-engineer** on identical cryptography tasks.

## Layout

- `TASKS/` — easy / medium / hard / adversarial task briefs
- `fixtures/` — intentional broken crypto + clean references
- `harness/` — scripts and run protocols
- `runs/` — session transcripts and graded artifacts
- `RUBRIC.md` — scoring dimensions
- `RESULTS.md` — baseline vs crypto scores
- `IMPROVEMENTS.md` — failure → patch mapping (Milestone 11)

## Protocol

1. Run each task with default agent (no crypto settings / without `--agent crypto-engineer`)
2. Run the same task with crypto specialization (`agent: crypto-engineer`)
3. Grade both with `RUBRIC.md` and expected-finding keys in each task file
4. Prefer compile/test/vector evidence over narrative alone

## Status

Scaffolded in Milestone 1; populated in Milestones 9–11.
