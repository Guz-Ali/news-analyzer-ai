package com.curatedNews.curatedNews.news.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.UUID;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "sources")
public class Source {
    @Id
    private UUID id;
    private String name;
    @Column(name = "base_link")
    private String baseLink;
    private String description;
}
