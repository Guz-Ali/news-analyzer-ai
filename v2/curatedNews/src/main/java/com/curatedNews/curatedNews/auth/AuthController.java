package com.curatedNews.curatedNews.auth;

import com.curatedNews.curatedNews.auth.model.AuthPayload;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/auth")
@RequiredArgsConstructor
public class AuthController {

    private final AuthService authService;

    @PostMapping("/{apiId}")
    public ResponseEntity<?> addCredentialsNewsApi(@PathVariable String apiId, @RequestBody AuthPayload payload) {
        authService.save(apiId, payload);
        return ResponseEntity.ok("API key stored for apiId: " + apiId);
    }

    @DeleteMapping("/{apiId}")
    public ResponseEntity<?> removeApiKey(@PathVariable String apiId) {
        authService.remove(apiId);
        return ResponseEntity.ok("API key removed for apiId: " + apiId);
    }

    @GetMapping("/{apiId}")
    public ResponseEntity<AuthPayload> getApiKey(@PathVariable String apiId) {
        return authService.get(apiId)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }
}

