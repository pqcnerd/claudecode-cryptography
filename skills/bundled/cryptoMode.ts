import { registerBundledSkill } from '../bundledSkills.js'

const CRYPTO_MODE_PROMPT = `# Crypto Mode — Decision Ladder

You are reinforcing **cryptography engineering** discipline for this session.

## Mode classification (state explicitly)

- **A — Production/application:** Prefer audited libraries (libsodium, RustCrypto, ring, BoringSSL/OpenSSL, WebCrypto, Tink). Do not invent primitives.
- **B — Implementation/research:** Implementing RFC/paper/arithmetic/ZK/PQC/FHE is expected. Spec→code→KAT→review. Do **not** nag "use a library."
- **Audit:** Prefer crypto-audit / crypto-spec-review / sidechannel-review agents.
- **Protocol:** Transcript-first; protocol-review skill.

## Ladder (abbreviated)

Security goal → threat model → mode → spec → properties → construction → library (A) or representation (B) → key lifecycle → nonce/IV → domain separation → serialization → transcript → attacks → implement → KATs → negative/property/differential tests → fuzz parsers → adversarial review → side-channel review → spec conformance → complete.

## Hard rules

- Never silently invent constructions.
- Never release plaintext before AEAD/MAC verification.
- Nonce/IV uniqueness is an API contract.
- No SHA*(password) for password storage.
- Separate keys by purpose; domain-separate contexts.
- Round-trip ≠ security. Prefer official vectors.
- Constant-time claims need language/runtime caveats.
- Mathematically correct ≠ cryptographically safe.

## Project specialization

If this repo has \`.claude/agents/crypto-engineer.md\` and \`.claude/skills/\`, prefer those procedural skills and spawn \`crypto-audit\`, \`crypto-verify\`, \`sidechannel-review\`, \`crypto-spec-review\` as appropriate.

See also: \`CLAUDE.md\`, \`.claude/ARCHITECTURE.md\`, \`CRYPTO_AGENT.md\`, \`evals/crypto/\`.
`

export function registerCryptoModeSkill(): void {
  registerBundledSkill({
    name: 'crypto-mode',
    description:
      'Activate cryptography-engineering decision ladder and Mode A/B discipline.',
    whenToUse:
      "Use at the start of cryptography tasks or when the user asks for crypto mode. Examples: 'crypto mode', 'think as a cryptographer', 'Mode B implementation'.",
    userInvocable: true,
    async getPromptForCommand(args) {
      const parts = [CRYPTO_MODE_PROMPT]
      if (args?.trim()) {
        parts.push(`## User Request\n\n${args.trim()}`)
      }
      return [{ type: 'text', text: parts.join('\n\n') }]
    },
  })
}
