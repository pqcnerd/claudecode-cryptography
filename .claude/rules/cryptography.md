# Cryptography engineering doctrine

This project prioritizes **cryptographic engineering** over generic application coding.

## Modes

- **A — Production:** Prefer libsodium, RustCrypto, ring, BoringSSL/OpenSSL, WebCrypto, Tink, established TLS/Noise stacks. Do not invent ciphers or modes.
- **B — Implementation/research:** Library, RFC, paper, arithmetic, ZK/PQC/FHE implementation is legitimate. Require spec, representation plan, vectors, and side-channel review for secret data. Do not block the user with "use a library."
- **Audit / Protocol:** Review-first; transcript-first for protocols.

## Always

- State security goal and mode before coding.
- Prefer authoritative specs (protocol → RFC/CFRG → NIST → official docs → reference impl → paper).
- Authenticate what you encrypt; fail closed on auth errors.
- Plan key hierarchy, nonce/IV strategy, domain separation, and serialization.
- Separate keys by purpose.
- Treat password storage as Argon2/scrypt (or documented legacy PBKDF2)—never SHA-*(password).
- Do not claim constant-time without caveats for the language/runtime.
- Require known-answer and negative tests for crypto changes when vectors exist.
- Round-trips alone do not prove security.

## Never

- Silently invent constructions.
- Return plaintext before verifying AEAD tags / MACs / signatures.
- Reuse nonces with the same key for nonce-respecting AEADs.
- Use ECB or unauthenticated CBC for new designs.
- Ambiguous length-free concatenation of variable fields in transcripts or signed messages.
- Log secrets, keys, nonces-with-key-material, or raw password-adjacent data.
