package com.curatedNews.curatedNews.news;

import com.curatedNews.curatedNews.news.apis.newsapi.NewsApiClient;
import com.curatedNews.curatedNews.news.model.News;
import com.curatedNews.curatedNews.news.model.Source;
import com.curatedNews.curatedNews.repositories.NewsRepository;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.time.ZoneOffset;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

@Slf4j
@Service
@AllArgsConstructor
public class NewsService {
    private final NewsRepository newsRepository;
    private final NewsApiClient newsApiClient;

    public List<News> getTodayNews() {
        var startOfDay = LocalDate.now().atStartOfDay().toInstant(ZoneOffset.UTC);
        var endOfDay = startOfDay.plusSeconds(86400);
        return newsRepository.findByGeneratedDateBetween(startOfDay, endOfDay);
    }

    public void generateNews() {
        List<News> externalNews;
        try {
            externalNews = new ArrayList<>(newsApiClient.generateNews()); //TODO: externalnews entity / record.
        } catch(Exception e) {
            log.error(e.getMessage());
            return;
        }

        List<News> entities = externalNews.stream().map(news -> {
            var src = news.getSource();
            var sourceEntity = new Source(
                src.getId(), src.getName(), src.getBaseLink(), src.getDescription()
            );

            return new News(
                news.getId() != null ? news.getId() : UUID.randomUUID(),
                news.getTitle(),
                news.getDescription(),
                news.getLink(),
                sourceEntity,
                news.getDate(),
                news.getGeneratedDate()
            );
        }).toList();

        newsRepository.saveAll(entities);
    }

}
