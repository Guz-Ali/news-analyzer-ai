package com.curatedNews.curatedNews.news.contacts;

import com.curatedNews.curatedNews.news.model.News;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class NewsClient {

    public List<News> generateNews() {
        return List.of();
    }
}
