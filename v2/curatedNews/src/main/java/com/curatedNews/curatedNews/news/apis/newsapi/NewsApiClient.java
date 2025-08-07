package com.curatedNews.curatedNews.news.apis.newsapi;

import com.curatedNews.curatedNews.news.model.News;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class NewsApiClient {

    public List<News> generateNews() {
        return List.of();
    }
}
