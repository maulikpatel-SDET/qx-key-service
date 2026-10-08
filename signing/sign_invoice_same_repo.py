from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

RSA_SIGNING_KEY = "keys/rsa_signing_private.pem"

def sign_invoice(invoice: bytes) -> bytes:
    with open(RSA_SIGNING_KEY, "rb") as fh:
        key = serialization.load_pem_private_key(fh.read(), password=None)
    return key.sign(invoice, padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                                         salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
