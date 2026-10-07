"""R3-08 KEY ROTATION: retire RSA-2048 (qx-rsa-1), activate RSA-3072 (qx-rsa-2). Manifest tells consumers which kid is active."""
import json
from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

KEYS = Path(__file__).resolve().parent.parent / "keys"


def rotate():
    new_key = rsa.generate_private_key(public_exponent=65537, key_size=3072)
    (KEYS / "rsa_signing_v2_public.pem").write_bytes(new_key.public_key().public_bytes(
        serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo))
    manifest = json.loads((KEYS / "rotation_manifest.json").read_text())
    for k in manifest["keys"]:
        k["status"] = "retired"
    manifest["keys"].append({"kid": "qx-rsa-2", "alg": "RS256", "size": 3072,
                             "file": "rsa_signing_v2_public.pem", "status": "active"})
    manifest["active"] = "qx-rsa-2"
    (KEYS / "rotation_manifest.json").write_text(json.dumps(manifest, indent=2))
