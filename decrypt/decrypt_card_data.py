"""R3-06 DECRYPT side: key-service decrypts card data with the RSA private key (never leaves this repo)."""
import os

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding


def decrypt_card(ciphertext: bytes) -> bytes:
    with open(os.environ["QX_ENCRYPTION_PRIVATE_KEY_PATH"], "rb") as fh:
        key = serialization.load_pem_private_key(fh.read(), password=None)
    return key.decrypt(ciphertext, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
