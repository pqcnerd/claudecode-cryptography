# Results: baseline vs crypto-engineer

## Fixture oracle smoke

```json
[
  {
    "fixture": "broken_aes_gcm_nonce_reuse.py",
    "auto_findings": [
      "nonce_reuse_or_fixed_nonce",
      "missing_nonce_uniqueness_discussion_in_code_comments"
    ]
  },
  {
    "fixture": "broken_password_sha256.py",
    "auto_findings": [
      "sha256_password_storage",
      "missing_password_kdf"
    ]
  },
  {
    "fixture": "broken_aes_ecb.py",
    "auto_findings": [
      "ecb_mode"
    ]
  },
  {
    "fixture": "broken_ct_compare.py",
    "auto_findings": [
      "early_return_compare"
    ]
  }
]
```

## Live run log

| Task ID | Baseline total | Crypto total | Notes |
|---------|---------------:|-------------:|-------|
| _(pending live sessions)_ | | | Populate from `runs/` |
| ADV-01 (expected) | typically misses or soft-flags | must hit `nonce_reuse_or_fixed_nonce` | See `runs/adv_01_expected_crypto.md` |

## Milestone 11 static patches

- Held-out task `heldout_01_key_reuse.md`
- Stronger AEAD plaintext-before-tag rule
- Explicit unauthenticated CBC / key-reuse hunt in `crypto-audit`
- CT `reference.md` + keyword routing table on main agent

## Milestone 12 productization

- Bundled `/crypto-mode` skill
- Built-in `crypto-engineer` agent fallback
- `CRYPTO_AGENT.md` launch docs

## Gate

Milestone 11 patches specialization when live crypto runs miss `expected_findings`. Re-run ADV-01..08 after live sessions.
