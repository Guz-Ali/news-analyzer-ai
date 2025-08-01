package com.curatedNews.curatedNews.news.model;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.Instant;
import java.util.UUID;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "news")
public class News{
    @Id
    private UUID id;
    private String title;
    private String description;
    private String link;
    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "source_id")
    private Source source;
    private Instant date;
    @Column(name = "generated_date")
    private Instant generatedDate;
}
