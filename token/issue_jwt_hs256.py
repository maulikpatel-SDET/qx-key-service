"""R3-03 SIGN side: HS256 (HMAC-SHA256) internal token. Secret comes from qx-infra-config."""
import os

import jwt


def issue_internal_token(service: str) -> str:
    return jwt.encode({"svc": service}, os.environ["JWT_HMAC_SECRET"], algorithm="HS256")
