"""CR-01 / CR-07 / CR-12 source: generate the RSA-2048 signing key shared by other repos."""
from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

OUT = Path(__file__).resolve().parent.parent / "keys"


def generate_rsa_signing_key():
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    OUT.mkdir(exist_ok=True)
    (OUT / "rsa_signing_private.pem").write_bytes(
        key.private_bytes(serialization.Encoding.PEM,
                          serialization.PrivateFormat.PKCS8,
                          serialization.NoEncryption()))
    (OUT / "rsa_signing_public.pem").write_bytes(
        key.public_key().public_bytes(serialization.Encoding.PEM,
                                      serialization.PublicFormat.SubjectPublicKeyInfo))


if __name__ == "__main__":
    generate_rsa_signing_key()
