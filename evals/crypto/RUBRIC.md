# Cryptography agent rubric

Score each dimension **0–3**:

| Score | Meaning |
|------:|---------|
| 0 | Missing / wrong / harmful |
| 1 | Vague partial awareness |
| 2 | Mostly correct with gaps |
| 3 | Precise, actionable, evidence-backed |

## Dimensions

1. Construction correctness
2. Specification correctness
3. API / misuse
4. Key management
5. Nonce / IV handling
6. Domain separation
7. Serialization
8. Side-channel awareness
9. Testing quality
10. Adversarial review quality
11. Final correctness
12. Mode classification

## Expected findings bonus

If a task lists `expected_findings`, +2 bonus when ≥80% of keys are explicitly hit.

Total = sum(dimensions) + bonus. Compare baseline vs crypto-engineer on the same task.
