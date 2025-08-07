package com.curatedNews.curatedNews.news;

import com.curatedNews.curatedNews.news.model.News;
import lombok.AllArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/news")
@AllArgsConstructor
public class NewsController {

    private final NewsService newsService;

    @GetMapping("/today")
    public ResponseEntity<List<News>> getTodayNews() {
        return ResponseEntity.ok(newsService.getTodayNews());
    }

    @PostMapping("/generate")
    public ResponseEntity<Void> generateNews() {
        newsService.generateNews();
        return ResponseEntity.ok().build();
    }
}
