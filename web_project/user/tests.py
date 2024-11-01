from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Profile
from django.urls import reverse


class TestModels(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", email="em@gmail.com", password="password"
        )
        self.client.login(username=self.user.username, password="password")

    def test_model_Profile(self):
        self.assertEquals(Profile.objects.count(), 1)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", email="em@gmail.com", password="password"
        )
        self.client.login(username=self.user.username, password="password")

        self.profile_url = reverse("profile")

    def test_profile_GET(self):
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 200)
