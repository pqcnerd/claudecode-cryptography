# EASY-03: HKDF session keys

**Prompt:** Derive separate client/server traffic keys from a shared secret for a handshake.

**expected_findings / behaviors:**
- hkdf_extract_expand
- distinct_info_labels
- key_separation

**difficulty:** easy
