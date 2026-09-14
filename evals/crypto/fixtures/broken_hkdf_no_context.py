"""BROKEN: HKDF with empty info used for unrelated purposes."""
# WARNING: intentionally insecure fixture
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

IKM = b"shared-secret"

def derive(purpose_ignored: str, length: int = 32) -> bytes:
    # missing domain separation / meaningful info
    return HKDF(algorithm=hashes.SHA256(), length=length, salt=None, info=b"").derive(IKM)
