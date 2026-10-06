"""CR-07 source: publish the RSA public key as a JWKS document (alg RS256)."""
import base64
import json
from pathlib import Path

from cryptography.hazmat.primitives import serialization

KEYS = Path(__file__).resolve().parent.parent / "keys"


def b64url(n: int) -> str:
    raw = n.to_bytes((n.bit_length() + 7) // 8, "big")
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()


def publish():
    pub = serialization.load_pem_public_key((KEYS / "rsa_signing_public.pem").read_bytes())
    nums = pub.public_numbers()
    jwks = {"keys": [{"kty": "RSA", "alg": "RS256", "use": "sig", "kid": "qx-rsa-1",
                      "n": b64url(nums.n), "e": b64url(nums.e)}]}
    (KEYS.parent / "jwks.json").write_text(json.dumps(jwks, indent=2))


if __name__ == "__main__":
    publish()
