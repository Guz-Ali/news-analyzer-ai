package com.curatedNews.curatedNews.auth.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.Customizer;
import org.springframework.security.config.annotation.web.configurers.AbstractHttpConfigurer;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;

@Configuration
public class SecurityConfig {

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/auth/**").hasRole("ADMIN")  // Secure only /auth/**
                .anyRequest().permitAll()
            )
            .httpBasic(Customizer.withDefaults()) // ✅ Modern replacement for .httpBasic()
            .csrf(AbstractHttpConfigurer::disable); // ✅ Modern replacement for .csrf().disable()

        return http.build();
    }
}
