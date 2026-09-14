"""BROKEN: AES-GCM with fixed nonce (nonce reuse). For audit evals only."""
# WARNING: intentionally insecure fixture
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

FIXED_NONCE = b"\x00" * 12
KEY = b"\x11" * 32

def encrypt(msg: bytes, aad: bytes = b"") -> bytes:
    # fixed_nonce reused for every message under the same key
    return AESGCM(KEY).encrypt(FIXED_NONCE, msg, aad)
