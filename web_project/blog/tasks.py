from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Post
import json
import google.generativeai as genai
from newsapi import NewsApiClient
import os
from django.conf import settings
import requests
import random


class NewsClient:
    def __init__(self):
        self._get_client_creds()
        self._set_client()
        super().__init__()

    def _get_client_creds(self):
        with open("/etc/config.json") as config_file:
            config = json.load(config_file)
        if not hasattr(self, "client_creds"):
            self.client_creds = {}
        self.client_creds["NEWS_API_KEY"] = config["NEWS_API_KEY"]
        self.creds = {}
        self.creds["GEMINI_API_KEY"] = config["GEMINI_API_KEY"]
        self.creds["NEWS_API_KEY"] = config["NEWS_API_KEY"]
        self.creds["PROMPT"] = config["PROMPT"]
        self.creds["AI_IMAGE"] = config["AI_IMAGE"] # There is no API currently in the server!

    def _set_client(self):
        self.client = NewsApiClient(api_key=self.client_creds["NEWS_API_KEY"])

    def get_sources(self, lang="en"):
        try:
            get_sources_json = self.client.get_sources(language=lang)
            if get_sources_json["status"] != "ok":
                raise ValueError
            sources_json = get_sources_json["sources"]
            sources_arr = []
            for source in sources_json:
                sources_arr.append(source["id"])
            sources = ",".join(sources_arr)
            return sources
        except ValueError as e:
            exit(e, "API call (get_sources) status NOT OK")

    def get_articles(self, sources):
        try:
            top_headlines = self.client.get_top_headlines(sources=sources)
            if top_headlines["status"] != "ok":
                raise ValueError
            articles = top_headlines["articles"]
            return articles
        except ValueError as e:
            exit(e, "API call (get_articles) status NOT OK")


class AIModel:
    def __init__(self):
        self._get_model_creds()
        self._set_model()
        super().__init__()

    def _get_model_creds(self):
        with open("/etc/config.json") as config_file:
            config = json.load(config_file)
        if not hasattr(self, "model_creds"):
            self.model_creds = {}
        self.model_creds["GEMINI_API_KEY"] = config["GEMINI_API_KEY"]
        self.model_creds["PROMPT"] = config["PROMPT"]

    def _set_model(self):
        genai.configure(api_key=self.model_creds["GEMINI_API_KEY"])
        self.model = genai.GenerativeModel("gemini-1.5-flash")


class AINewsGenerator(NewsClient, AIModel):
    def __init__(self):
        super().__init__()

    def prepare_prompt(self, articles):
        all_news = []
        for article in articles:
            if not (
                article["source"]["name"]
                and article["title"]
                and article["description"]
                and article["publishedAt"]
                and article["content"]
                and article["url"]
            ):
                continue
            news = []
            news.append(article["source"]["name"])
            news.append("\n")
            news.append(article["title"])
            news.append("\n")
            news.append(article["description"])
            news.append("\n")
            news.append(article["publishedAt"])
            news.append("\n")
            news.append(article["content"])
            news.append("\n")
            news.append(article["url"])
            news.append("\n\n")
            news_string = "".join(news)
            all_news.append(news_string)

        all_news.append(self.model_creds["PROMPT"])
        return all_news

    def collect_news(self):
        sources = self.get_sources()
        articles = self.get_articles(sources)
        prompt = self.prepare_prompt(articles)
        return prompt

    def generate_ai_text(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text
    
    def generate_ai_image(self, prompt):
        api_key = self.creds["AI_IMAGE"]
        r = requests.post(
            "https://api.deepai.org/api/text2img",
            data={
                'text': f'create a header image for this news, make it realistic: {prompt}',
            },
            headers={'api-key': api_key}
        )
        
        
        
        if r.status_code != 200:
            return "ai_images/ai_default.jpg"
        else:
            image_url = r.json().get("output_url")
            if image_url:
                output_dir = os.path.join(settings.MEDIA_ROOT, 'ai_images')
                os.makedirs(output_dir, exist_ok=True)
                filename = f"image_{random.randint(0, 100000)}.jpg"
                image_path = os.path.join(output_dir, filename)
                
                response = requests.get(image_url)
                if response.status_code == 200:
                    with open(image_path, 'wb') as f:
                        f.write(response.content)
                    return f"ai_images/{filename}"

        

    def create_ai_post(self, ai_news_text):
        ai_post = Post(
            title="Today's News",
            content=ai_news_text,
            date_posted=timezone.now(),
            author=get_object_or_404(User, username="enesdemirel"),
        )
        ai_post.save()
