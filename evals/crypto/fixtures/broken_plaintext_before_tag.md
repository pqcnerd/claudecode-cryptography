# BROKEN: plaintext released before AEAD tag check

pt = decrypt_ctr(key, nonce, ciphertext)
deliver_to_app(pt)   # TOO EARLY
verify_tag(tag)

Expected finding: plaintext_before_tag_verification
