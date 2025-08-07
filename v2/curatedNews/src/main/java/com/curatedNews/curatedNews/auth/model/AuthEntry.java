package com.curatedNews.curatedNews.auth.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Table(name = "auth_entries")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class AuthEntry {
    @Id
    private String id;

    @Column(nullable = false)
    private String data;
}
