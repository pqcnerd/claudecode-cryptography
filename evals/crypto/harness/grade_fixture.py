#!/usr/bin/env python3
"""Grade intentional crypto fixtures by static checks and simple oracles."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "fixtures"


def grade_nonce_reuse(path: Path) -> dict:
    text = path.read_text()
    findings = []
    if "NONCE = " in text or "nonce = b\"\\x00" in text or "fixed_nonce" in text:
        findings.append("nonce_reuse_or_fixed_nonce")
    if "AES" in text and "GCM" in text and "nonce" in text.lower():
        if "unique" not in text.lower() and "counter" not in text.lower():
            findings.append("missing_nonce_uniqueness_discussion_in_code_comments")
    return {"fixture": path.name, "auto_findings": findings}


def grade_password_sha(path: Path) -> dict:
    text = path.read_text()
    findings = []
    if "sha256" in text.lower() and "password" in text.lower():
        findings.append("sha256_password_storage")
    if "argon2" not in text.lower() and "scrypt" not in text.lower():
        findings.append("missing_password_kdf")
    return {"fixture": path.name, "auto_findings": findings}


def grade_ecb(path: Path) -> dict:
    text = path.read_text()
    findings = []
    if "ECB" in text or "AES_ECB" in text or "MODE_ECB" in text:
        findings.append("ecb_mode")
    return {"fixture": path.name, "auto_findings": findings}


def grade_ct_compare(path: Path) -> dict:
    text = path.read_text()
    findings = []
    if "if left[i] != right[i]" in text or "return False" in text and "for " in text:
        findings.append("early_return_compare")
    if "==" in text and "mac" in text.lower():
        findings.append("possibly_non_constant_time_mac_compare")
    return {"fixture": path.name, "auto_findings": findings}


GRADERS = {
    "broken_aes_gcm_nonce_reuse.py": grade_nonce_reuse,
    "broken_password_sha256.py": grade_password_sha,
    "broken_aes_ecb.py": grade_ecb,
    "broken_ct_compare.py": grade_ct_compare,
}


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: grade_fixture.py <fixture-file>")
        print("Available:", ", ".join(GRADERS))
        return 2
    name = Path(sys.argv[1]).name
    path = FIX / name
    if not path.exists():
        print(json.dumps({"error": f"missing {path}"}))
        return 1
    grader = GRADERS.get(name)
    if not grader:
        print(json.dumps({"error": f"no grader for {name}", "hint": list(GRADERS)}))
        return 1
    print(json.dumps(grader(path), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
