"""R3-05 PRIVATE KEY side: key-service signs receipts with ECDSA P-256."""
from pathlib import Path

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec

KEYS = Path(__file__).resolve().parent.parent / "keys"


def sign_receipt(receipt: bytes) -> bytes:
    key = serialization.load_pem_private_key((KEYS / "ec_signing_private.pem").read_bytes(), password=None)
    return key.sign(receipt, ec.ECDSA(hashes.SHA256()))
