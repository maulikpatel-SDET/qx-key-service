// R3-07 KEY OWNER side: key-service creates the ML-KEM-768 key pair, publishes the public key,
// and decapsulates what payment-service sends.
package com.qx.keys;

import java.nio.file.Files;
import java.nio.file.Path;
import java.security.KeyFactory;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.SecureRandom;
import java.security.Security;
import java.security.spec.PKCS8EncodedKeySpec;
import javax.crypto.KeyGenerator;

import org.bouncycastle.jcajce.SecretKeyWithEncapsulation;
import org.bouncycastle.jcajce.spec.KEMExtractSpec;
import org.bouncycastle.jcajce.spec.MLKEMParameterSpec;
import org.bouncycastle.jce.provider.BouncyCastleProvider;

public class MlKemKeyService {
    public static void createKeys() throws Exception {
        Security.addProvider(new BouncyCastleProvider());
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("ML-KEM", "BC");
        kpg.initialize(MLKEMParameterSpec.ml_kem_768, new SecureRandom());
        KeyPair kp = kpg.generateKeyPair();
        Files.write(Path.of("keys/mlkem_public.key"), kp.getPublic().getEncoded());
        Files.write(Path.of("keys/mlkem_private.key"), kp.getPrivate().getEncoded());
    }

    public static byte[] decapsulate(byte[] encapsulation) throws Exception {
        Security.addProvider(new BouncyCastleProvider());
        PrivateKey sk = KeyFactory.getInstance("ML-KEM", "BC")
                .generatePrivate(new PKCS8EncodedKeySpec(Files.readAllBytes(Path.of("keys/mlkem_private.key"))));
        KeyGenerator kg = KeyGenerator.getInstance("ML-KEM", "BC");
        kg.init(new KEMExtractSpec(sk, encapsulation, "AES"));
        return ((SecretKeyWithEncapsulation) kg.generateKey()).getEncoded();
    }
}
