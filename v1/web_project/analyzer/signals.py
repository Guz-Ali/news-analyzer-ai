from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Analysis
from .tasks import createPostFromAnalysis
from blog.models import Post


@receiver(post_save, sender=Analysis)
def create_analysis_post(sender, instance, created, **kwargs):
    if created:
        createPostFromAnalysis(instance)
