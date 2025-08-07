package com.curatedNews.curatedNews.auth.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.crypto.encrypt.Encryptors;
import org.springframework.security.crypto.encrypt.TextEncryptor; // ✅ REQUIRED

@Configuration
public class EncryptionConfig {

    @Bean
    public TextEncryptor textEncryptor() {
        // Can come from env vars or hardcoded during dev
        String password = "some-password"; // TODO: pull from vault/env in prod
        String salt = "deadbeef12345678";  // TODO: 16 hex chars
        return Encryptors.text(password, salt);
    }
}

