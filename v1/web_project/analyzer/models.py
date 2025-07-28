from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse


class Analysis(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=50)
    prompt = models.CharField(max_length=100)
    findings = models.TextField(blank=True)
    date_range_start = models.DateTimeField(default=datetime.min)
    date_range_end = models.DateTimeField(default=timezone.now)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("analysis-detail", kwargs={"pk": self.pk})
