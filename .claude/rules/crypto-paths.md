---
paths:
  - "**/crypto/**"
  - "**/*cipher*"
  - "**/*aead*"
  - "**/*sign*"
  - "**/*verify*"
  - "**/*proof*"
  - "**/*zk*"
  - "**/field/**"
  - "**/*curve*"
  - "**/*pairing*"
  - "**/*kdf*"
  - "**/*hmac*"
  - "**/*hash*"
  - "**/*mac*"
  - "**/*nonce*"
  - "**/*secret*"
  - "**/*tls*"
  - "**/*noise*"
  - "**/*pqc*"
  - "**/*lattice*"
  - "**/*ntt*"
  - "**/*fhe*"
  - "**/mpc/**"
  - "**/secureStorage/**"
  - "**/*ecdsa*"
  - "**/*eddsa*"
  - "**/*x25519*"
  - "**/*kyber*"
  - "**/*dilithium*"
  - "**/*falcon*"
---

# Path-scoped cryptography rules

You are editing cryptography-related code. Raise the bar:

1. Label values as **secret** or **public**.
2. Name the construction and governing spec/section when applicable.
3. Check nonce/IV, domain separation, and canonical encoding.
4. For Mode B / low-level code: consider constant-time behavior and reject non-canonical / invalid points or encodings at the boundary.
5. Add or update KATs / negative tests with the change.
6. Prefer spawning `crypto-audit`, `crypto-verify`, `sidechannel-review`, or `crypto-spec-review` before calling the work complete.
7. Do not "simplify" crypto by removing authentication, validation, or domain separation.
