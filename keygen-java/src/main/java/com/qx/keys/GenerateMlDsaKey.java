// CR-03 / CR-04 source: generate the ML-DSA-65 key pair used by qx-payment-service.
package com.qx.keys;

import java.nio.file.Files;
import java.nio.file.Path;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.SecureRandom;
import java.security.Security;

import org.bouncycastle.jcajce.spec.MLDSAParameterSpec;
import org.bouncycastle.jce.provider.BouncyCastleProvider;

public class GenerateMlDsaKey {
    public static void main(String[] args) throws Exception {
        Security.addProvider(new BouncyCastleProvider());
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("ML-DSA", "BC");
        kpg.initialize(MLDSAParameterSpec.ml_dsa_65, new SecureRandom());
        KeyPair kp = kpg.generateKeyPair();

        Path keys = Path.of("keys");
        Files.createDirectories(keys);
        Files.write(keys.resolve("mldsa_public.key"), kp.getPublic().getEncoded());   // X.509 SPKI
        Files.write(keys.resolve("mldsa_private.key"), kp.getPrivate().getEncoded()); // PKCS#8
    }
}
