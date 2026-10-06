// CR-04 source: key-service has MIGRATED token signing to ML-DSA-65.
package com.qx.keys;

import java.nio.file.Files;
import java.nio.file.Path;
import java.security.KeyFactory;
import java.security.PrivateKey;
import java.security.Security;
import java.security.Signature;
import java.security.spec.PKCS8EncodedKeySpec;

import org.bouncycastle.jce.provider.BouncyCastleProvider;

public class TokenIssuer {
    public static byte[] issue(byte[] token) throws Exception {
        Security.addProvider(new BouncyCastleProvider());
        byte[] der = Files.readAllBytes(Path.of("keys/mldsa_private.key"));
        PrivateKey key = KeyFactory.getInstance("ML-DSA", "BC").generatePrivate(new PKCS8EncodedKeySpec(der));
        Signature s = Signature.getInstance("ML-DSA", "BC");
        s.initSign(key);
        s.update(token);
        return s.sign();
    }
}
