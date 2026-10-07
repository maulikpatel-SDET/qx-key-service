"""R3-04 PRIVATE KEY side: key-service signs documents with the RSA private key (PKCS#1 v1.5)."""
from pathlib import Path

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

KEYS = Path(__file__).resolve().parent.parent / "keys"


def sign_document(document: bytes) -> bytes:
    private_key = serialization.load_pem_private_key(
        (KEYS / "rsa_signing_private.pem").read_bytes(), password=None)
    return private_key.sign(document, padding.PKCS1v15(), hashes.SHA256())
