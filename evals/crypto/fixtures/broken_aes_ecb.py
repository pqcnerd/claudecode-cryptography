"""BROKEN: AES-ECB for 'encryption'. For audit evals only."""
# WARNING: intentionally insecure fixture
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

KEY = b"\x22" * 16

def encrypt_block_aligned(pt: bytes) -> bytes:
    assert len(pt) % 16 == 0
    encryptor = Cipher(algorithms.AES(KEY), modes.ECB()).encryptor()
    return encryptor.update(pt) + encryptor.finalize()
