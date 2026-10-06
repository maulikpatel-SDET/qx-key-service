"""CR-02 source: generate the ECDSA P-256 key used by the Go payment service."""
from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

OUT = Path(__file__).resolve().parent.parent / "keys"


def generate_ec_signing_key():
    key = ec.generate_private_key(ec.SECP256R1())
    OUT.mkdir(exist_ok=True)
    (OUT / "ec_signing_private.pem").write_bytes(
        key.private_bytes(serialization.Encoding.PEM,
                          serialization.PrivateFormat.PKCS8,
                          serialization.NoEncryption()))


if __name__ == "__main__":
    generate_ec_signing_key()
