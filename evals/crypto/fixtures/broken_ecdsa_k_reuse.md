# BROKEN ECDSA sketch (nonce k reuse)

Signing two messages with the same ephemeral nonce `k` and private key `d` allows recovery of `d`.

Expected finding: ecdsa_nonce_reuse
