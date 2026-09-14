---
name: key-lifecycle
description: Design key generation, derivation, storage, rotation, revocation, backup, and destruction.
when_to_use: Use whenever keys exist. Examples: 'key hierarchy', 'envelope encryption', 'rotate DEKs', 'KMS design'.
---

# key-lifecycle

## Inputs
- Key purposes; storage platform (KMS/HSM/OS keychain/file); multi-tenant needs

## Procedure
Walk and document:
generation → derivation → storage → loading → use → rotation → revocation → backup/recovery → destruction

1. Separate KEKs and DEKs; envelope encryption where appropriate.
2. Key IDs and versioning on ciphertexts.
3. Privilege separation for create/use/delete.
4. Rotation: re-encrypt vs dual-accept windows; old ciphertext handling.
5. Compromise response playbook.
6. Backup/recovery without weakening secrecy (split knowledge / HSM).
7. Zeroization limitations by language—be honest.

## Required output
```
Key hierarchy:
IDs/versioning:
Storage:
Rotation:
Compromise response:
Destruction notes:
```

## Failure conditions
- Single master key used for unrelated purposes
- No kid/version on ciphertext
- Logging key material

## Verification
Rotation drill; decrypt after rotation; access-denied paths tested.
