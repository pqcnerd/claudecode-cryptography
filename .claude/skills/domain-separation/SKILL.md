---
name: domain-separation
description: Design cryptographic domain separation labels and context binding.
when_to_use: Use whenever one key/hash/signature scheme serves multiple purposes or protocols. Examples: 'domain separate HKDF', 'label this transcript', 'prevent cross-protocol signing'.
---

# domain-separation

## Inputs
- Protocols, versions, message types, key purposes

## Procedure
1. List all contexts sharing hash/MAC/sign/KDF keys.
2. Assign unique, explicit labels (protocol name, version, message type, purpose).
3. Prefer length-prefixed or fixed structured encodings over raw concatenation.
4. Bind identities, algorithm IDs, and channel parameters where relevant.
5. Ensure verifiers reject wrong-domain messages.
6. Document labels in SPEC→CODE map.

## Required output
```
Contexts:
Labels:
Encoding of label||fields:
Negative tests:
```

## Failure conditions
- Same signature bytes valid across chains/intents
- HKDF info empty across different purposes
- Ambiguous concatenation of variable-length fields

## Verification
Cross-domain verification attempts fail.
