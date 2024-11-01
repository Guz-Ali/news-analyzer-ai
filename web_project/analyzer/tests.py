from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Analysis
from blog.models import Post
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
        self.user_login = User.objects.create_user(
            username="testuser", email="em@gmail.com", password="password"
        )
        self.user_other = User.objects.create_user(
            username="testuser_2", email="em@gmail.com", password="password_2"
        )
        self.client.login(username=self.user_login.username, password="password")

        self.analysis = Analysis.objects.create(
            title="test_analysis",
            keywords="test1,test2",
            prompt="this is a test",
            findings="",
            date_range_start=datetime.min,
            date_range_end=timezone.now(),
            date_posted=timezone.now(),
            author=self.user_login,
        )

        self.analysis_other = Analysis.objects.create(
            title="test_analysis_other",
            keywords="test1,test2",
            prompt="this is a test",
            findings="",
            date_range_start=datetime.min,
            date_range_end=timezone.now(),
            date_posted=timezone.now(),
            author=self.user_other,
        )

        self.analysis_create_url = reverse("analyzer-home")
        self.analysis_detail_url = reverse("analysis-detail", args=[self.analysis.id])
        self.analysis_other_detail_url = reverse(
            "analysis-detail", args=[self.analysis_other.id]
        )
        self.analysis_publish_url = reverse("analysis-publish", args=[self.analysis.id])
        self.analysis_other_publish_url = reverse(
            "analysis-publish", args=[self.analysis_other.id]
        )
        self.analysis_delete_url = reverse("analysis-delete", args=[self.analysis.id])
        self.user_analyses_url = reverse(
            "user-analyses", args=[self.user_login.username]
        )
        self.user_other_analyses_url = reverse(
            "user-analyses", args=[self.user_other.username]
        )
        self.analysis_post_delete_url = reverse(
            "post-delete", args=[Post.objects.get(title="test_analysis").id]
        )

    def test_analysis_detail_GET(self):
        response = self.client.get(self.analysis_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTrue(isinstance(response.context["object"], Analysis))

    def test_analysis_other_detail_GET(self):
        response = self.client.get(self.analysis_other_detail_url)

        self.assertEquals(response.status_code, 403)

    def test_user_analyses_GET(self):
        response = self.client.get(self.user_analyses_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            Analysis.objects.filter(author=self.user_login.id).count(),
            len(response.context["object_list"]),
        )

    def test_user_other_analyses_GET(self):
        response = self.client.get(self.user_other_analyses_url)

        self.assertEquals(response.status_code, 403)

    def test_analysis_create_POST(self):
        response = self.client.post(
            self.analysis_create_url,
            {
                "title": "test_analysis_create",
                "keywords": "test1,test2",
                "prompt": "this is a test",
                "findings": "",
                "date_range_start": datetime.min,
                "date_range_end": timezone.now(),
                "date_posted": timezone.now(),
                "author": self.user_login.id,
            },
        )
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Analysis.objects.count(), 3)
        self.assertEquals(Analysis.objects.last().title, "test_analysis_create")
        self.assertEquals(Post.objects.last().title, "test_analysis_create")
        self.assertEquals(Post.objects.last().is_public, False)

    def test_analysis_publish_POST(self):
        response = self.client.post(self.analysis_publish_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(Post.objects.get(title="test_analysis").is_public, True)

    def test_analysis_other_publish_POST(self):
        response = self.client.post(self.analysis_other_publish_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(Post.objects.get(title="test_analysis").is_public, False)

    def test_analysis_delete_DELETE(self):
        response = self.client.delete(self.analysis_delete_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Analysis.objects.count(), 1)
        self.assertEquals(Post.objects.count(), 1)

    def test_analysis_post_delete_DELETE(self):
        self.test_analysis_publish_POST()
        response = self.client.delete(self.analysis_post_delete_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Analysis.objects.count(), 2)
        self.assertEquals(Post.objects.count(), 1)

    def test_analysis_and_post_delete_DELETE(self):
        self.test_analysis_post_delete_DELETE()
        self.test_analysis_delete_DELETE()

    def test_analysis_post_delete_publish_POST(self):
        self.test_analysis_post_delete_DELETE()

        response = self.client.post(self.analysis_publish_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Analysis.objects.count(), 2)
        self.assertEquals(Post.objects.last().title, "test_analysis")
        self.assertEquals(Post.objects.last().is_public, True)
