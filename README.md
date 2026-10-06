# qx-key-service  (Repo 1 of 4)

Generates and publishes all keys used by the other repos.
TEST KEYS ONLY - generated for Qryptive testing, never used in production.

| File | What it creates | Used by |
|---|---|---|
| keygen/generate_rsa_key.py | RSA-2048 signing key -> keys/rsa_signing_private.pem | qx-payment-service (CR-01, CR-07, CR-12) |
| keygen/generate_ec_key.py | ECDSA P-256 key -> keys/ec_signing_private.pem | qx-payment-service Go (CR-02) |
| keygen-java/.../GenerateMlDsaKey.java | ML-DSA-65 key -> keys/mldsa_public.key | qx-payment-service Java (CR-03, CR-04) |
| keygen/publish_jwks.py | jwks.json (RS256) | qx-payment-service (CR-07) |
| certs/server.crt | RSA-2048 TLS certificate | qx-infra-config nginx (CR-08) |
| keys/test_ec_private.pem | committed private key (test) | qx-payment-service (CR-09) |
