"""R3-02 SIGN side: key-service issues an ES256 JWT (ECDSA P-256) for the Go service."""
import time
from pathlib import Path

import jwt

KEYS = Path(__file__).resolve().parent.parent / "keys"


def issue_settlement_token(batch_id: str) -> str:
    private_pem = (KEYS / "ec_signing_private.pem").read_bytes()
    claims = {"batch": batch_id, "iss": "qx-key-service", "exp": int(time.time()) + 300}
    return jwt.encode(claims, private_pem, algorithm="ES256")
