# Held-out: key reuse across purposes

**Prompt:** An app uses one 256-bit key for AES-GCM file encryption and also as the HMAC key for API request auth. Review this design.

**expected_findings:**
- key_reuse_across_purposes
- recommend_kdf_or_separate_keys
- domain_separation_or_key_separation

**difficulty:** held-out
**notes:** Do not use solely for overfitting patches; keep as holdout when tuning prompts.
