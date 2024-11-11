from django.core.management.base import BaseCommand
from blog.models import NewsCard
from blog.utils import newsParser
from django.utils import timezone
from blog.tasks import AINewsGenerator
import os
from django.utils import timezone

def create_newscard(text_block):
    news_items = newsParser(text_block)

    for index, item in enumerate(news_items, start=1):
        print(f"DEBUG: Processing news item {index} - Title: {item['title']}")

        try:
            # Temporary fix for image generation because we are out of credits.
            image_filename = "default.jpg" 
            print(f"DEBUG: Using default image for news item {index}")

            # image_filename = AINewsGenerator().generate_ai_image(item['title'] + " " + item['content'])

            news_card = NewsCard(
                title=item['title'],
                content=item['content'],
                date_posted=timezone.now(),
                date_created=timezone.now(),
                url_of_the_news=item['link'],
                summary=item['content'][:500],
                is_public=True
            )

            news_card.image = image_filename

            news_card.save()
            print(f"DEBUG: NewsCard saved for item {index} - Title: {item['title']}")

        except Exception as e:
            print(f"ERROR: Failed to save news item {index} - Title: {item['title']}")
            print(f"Exception: {e}")

class Command(BaseCommand):
    help = 'Generates AI news posts and creates individual news cards.'

    def handle(self, *args, **options):
        ai_news_generator = AINewsGenerator()
        text_block = ai_news_generator.generate_ai_text(ai_news_generator.collect_news())

        create_newscard(text_block)

        self.stdout.write(self.style.SUCCESS("Successfully created news cards"))
