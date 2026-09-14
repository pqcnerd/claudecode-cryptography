"""BROKEN: AES-CBC without MAC. For audit evals."""
# WARNING: intentionally insecure fixture
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

KEY = b"\x33" * 16

def encrypt(pt: bytes) -> bytes:
    iv = os.urandom(16)
    padder = padding.PKCS7(128).padder()
    data = padder.update(pt) + padder.finalize()
    enc = Cipher(algorithms.AES(KEY), modes.CBC(iv)).encryptor()
    return iv + enc.update(data) + enc.finalize()
