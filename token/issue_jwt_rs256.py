"""R3-01 SIGN side: key-service issues an RS256 JWT with its RSA private key."""
import time
from pathlib import Path

import jwt

KEYS = Path(__file__).resolve().parent.parent / "keys"


def issue_access_token(user_id: str) -> str:
    private_pem = (KEYS / "rsa_signing_private.pem").read_bytes()
    claims = {"sub": user_id, "iss": "qx-key-service", "exp": int(time.time()) + 900}
    return jwt.encode(claims, private_pem, algorithm="RS256", headers={"kid": "qx-rsa-1"})
