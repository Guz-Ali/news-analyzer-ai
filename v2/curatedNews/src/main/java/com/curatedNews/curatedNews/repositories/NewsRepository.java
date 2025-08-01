package com.curatedNews.curatedNews.repositories;

import com.curatedNews.curatedNews.news.model.News;
import com.curatedNews.curatedNews.news.model.Source;
import org.springframework.data.jpa.repository.JpaRepository;

import java.time.Instant;
import java.util.List;
import java.util.UUID;

public interface NewsRepository extends JpaRepository<News, UUID> {
    List<News> findAllBySource(Source source);

    List<News> findByGeneratedDateBetween(Instant startOfDay, Instant endOfDay);
}
