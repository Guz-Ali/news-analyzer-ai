from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Analysis
from django.utils import timezone
from datetime import datetime
from django.urls import reverse


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="em@gmail.com", password="password"
        )

    def test_model_Analysis(self):
        analysis = Analysis.objects.create(
            title="test_analysis",
            keywords="test1,test2",
            prompt="this is a test",
            findings="",
            date_range_start=datetime.min,
            date_range_end=timezone.now(),
            date_posted=timezone.now(),
            author=self.user,
        )

        self.assertEquals(str(analysis), "test_analysis")
        self.assertTrue(isinstance(analysis, Analysis))


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", email="em@gmail.com", password="password"
        )
        self.client.login(username=self.user.username, password="password")

        self.analysis = Analysis.objects.create(
            title="test_analysis",
            keywords="test1,test2",
            prompt="this is a test",
            findings="",
            date_range_start=datetime.min,
            date_range_end=timezone.now(),
            date_posted=timezone.now(),
            author=self.user,
        )

        self.analysis_create_url = reverse("analyzer-home")
        self.analysis_detail = reverse("analysis-detail", args=[self.analysis.id])

    def test_analysis_detail_GET(self):
        response = self.client.get(self.analysis_detail)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Analysis.objects.count(), 1)

    def test_analysis_create_POST(self):
        response = self.client.post(
            self.analysis_create_url,
            {
                "title": "test_analysis",
                "keywords": "test1,test2",
                "prompt": "this is a test",
                "findings": "",
                "date_range_start": datetime.min,
                "date_range_end": timezone.now(),
                "date_posted": timezone.now(),
                "author": self.user.id,
            },
        )
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Analysis.objects.count(), 2)
        self.assertEquals(Analysis.objects.last().title, "test_analysis")
