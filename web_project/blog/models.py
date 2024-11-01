from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from analyzer.models import Analysis


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)
    analysis = models.OneToOneField(
        Analysis, blank=True, null=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

class NewsCard(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) 
    date_created = models.DateTimeField(auto_now_add=True)
    url_of_the_news = models.URLField()
    summary = models.TextField(max_length=100) #can be changed later.
    image = models.ImageField(upload_to='ai_images/', null= True, blank= True, default="ai_default.jpg")
    is_public = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})