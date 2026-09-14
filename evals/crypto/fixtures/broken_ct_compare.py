"""BROKEN: early-return MAC compare. For side-channel evals."""
# WARNING: intentionally insecure fixture

def mac_compare(left: bytes, right: bytes) -> bool:
    if len(left) != len(right):
        return False
    for i in range(len(left)):
        if left[i] != right[i]:
            return False  # early_return_compare
    return True
