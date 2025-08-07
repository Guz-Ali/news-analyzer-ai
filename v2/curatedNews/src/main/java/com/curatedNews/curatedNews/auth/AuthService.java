package com.curatedNews.curatedNews.auth;

import com.curatedNews.curatedNews.auth.model.AuthPayload;
import com.curatedNews.curatedNews.auth.model.AuthEntry;
import com.curatedNews.curatedNews.repositories.AuthRepository;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.security.crypto.encrypt.TextEncryptor;
import org.springframework.stereotype.Service;


import java.util.List;
import java.util.Optional;

@Service
@Slf4j
@RequiredArgsConstructor
public class AuthService {
    private final AuthRepository authRepository;
    private final TextEncryptor encryptor;
    private final ObjectMapper objectMapper;

    public Optional<AuthPayload> get(String id) {
        return authRepository.findById(id)
            .map(AuthEntry::getData)
            .map(encryptor::decrypt)
            .map(json -> {
                try {
                    return objectMapper.readValue(json, AuthPayload.class);
                } catch (Exception e) {
                    log.error("Failed to parse decrypted JSON for ID {}", id, e);
                    return null;
                }
            });
    }

    public void save(String id, AuthPayload payload) {
        try {
            String json = objectMapper.writeValueAsString(payload);
            String encrypted = encryptor.encrypt(json);
            authRepository.save(new AuthEntry(id, encrypted));
        } catch (Exception e) {
            log.error("Failed to save credential for ID {}", id, e);
        }
    }

    public void remove(String id) {
        authRepository.deleteById(id);
    }

    public List<String> listIds() {
        return authRepository.findAll().stream()
            .map(AuthEntry::getId)
            .toList();
    }
}

