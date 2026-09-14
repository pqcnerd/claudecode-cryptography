"""BROKEN: SHA256(password) storage. For audit evals only."""
# WARNING: intentionally insecure fixture
import hashlib

def store_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password: str, stored: str) -> bool:
    return store_password(password) == stored
