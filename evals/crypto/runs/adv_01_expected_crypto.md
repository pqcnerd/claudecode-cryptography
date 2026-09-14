# Sample expected crypto-audit behavior (ADV-01)

**Task:** Audit `evals/crypto/fixtures/broken_aes_gcm_nonce_reuse.py`

**Expected Mode:** Audit

**Expected finding (minimum):**

```
SEVERITY: critical
LOCATION: broken_aes_gcm_nonce_reuse.py encrypt()/FIXED_NONCE
CRYPTOGRAPHIC ISSUE: AES-GCM nonce reuse under a fixed key
WHY IT MATTERS: Nonce reuse with GCM enables forgery / catastrophic authenticity failure
ATTACK / FAILURE MODEL: Two ciphertexts under same key+nonce leak plaintext relations and allow attackers to forge tags for other messages
RECOMMENDED FIX: Unique nonces per encryption (counter with persistence or 96-bit+ random with collision bounds); or XChaCha20-Poly1305 / AES-GCM-SIV where misuse resistance is required; never hard-code FIXED_NONCE
VERIFICATION: Unit test that fails if duplicate nonces observed; code search for constant nonces
```

**Oracle:** `python3 evals/crypto/harness/grade_fixture.py broken_aes_gcm_nonce_reuse.py` → `nonce_reuse_or_fixed_nonce`
