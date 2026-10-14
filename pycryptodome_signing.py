"""R5-01 PyCryptodome (not 'cryptography'): RSA PKCS#1 v1.5 signing + ECC P-256 DSS signing."""
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC, RSA
from Crypto.Signature import DSS, pkcs1_15


def sign_both(message: bytes):
    rsa_key = RSA.generate(2048)
    rsa_sig = pkcs1_15.new(rsa_key).sign(SHA256.new(message))

    ec_key = ECC.generate(curve="P-256")
    ec_sig = DSS.new(ec_key, "fips-186-3").sign(SHA256.new(message))
    return rsa_sig, ec_sig
