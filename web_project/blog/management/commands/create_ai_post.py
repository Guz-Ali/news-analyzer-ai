from django.core.management.base import BaseCommand, CommandError
from blog.tasks import AINewsGenerator

class Command(BaseCommand):
    help = "Generates an AI News Post from top headlines"

    def handle(self, *args, **options):
        ai_news_generator = AINewsGenerator()
        news_prompt = ai_news_generator.collect_news()
        ai_news_text = ai_news_generator.generate_ai_text(news_prompt)
        # prompt = "A bird swimming in the pool." # To be changed later with the single news prompt.
        # file_name = ai_news_generator.generate_ai_image(prompt)
        ai_news_generator.create_ai_post(ai_news_text)
        self.stdout.write(
            self.style.SUCCESS("Successfully generated AI News Post")
        )

