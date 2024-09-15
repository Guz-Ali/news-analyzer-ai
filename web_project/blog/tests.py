from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Post
from django.utils import timezone
from django.urls import reverse


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")

    def test_model_Post(self):
        post = Post.objects.create(
            title="test_post",
            content="test_content",
            date_posted=timezone.now(),
            author=self.user,
        )

        self.assertEquals(str(post), "test_post")
        self.assertTrue(isinstance(post, Post))


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", email="em@gmail.com", password="password"
        )
        self.client.login(username=self.user.username, password="password")

        self.post = Post.objects.create(
            title="test_post_2",
            content="test_content_2",
            date_posted=timezone.now(),
            author=self.user,
        )

        self.home_url = reverse("blog-home")
        self.post_create_url = reverse("post-create")
        self.post_detail_url = reverse("post-detail", args=[self.post.id])
        self.post_edit_url = reverse("post-update", args=[self.post.id])
        self.post_delete_url = reverse("post-delete", args=[self.post.id])

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/home.html")

    def test_post_detail_GET(self):
        response = self.client.get(self.post_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Post.objects.count(), 1)

    def test_post_create_POST(self):
        response = self.client.post(
            self.post_create_url,
            {
                "title": "test_post_3",
                "content": "test_content_3",
                "date_posted": timezone.now(),
                "author": self.user.id,
            },
        )

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Post.objects.count(), 2)
        self.assertEquals(Post.objects.last().title, "test_post_3")

    def test_post_create_POST_no_data(self):
        response = self.client.post(self.post_create_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Post.objects.count(), 1)

    def test_post_edit_POST(self):
        response = self.client.post(
            self.post_edit_url,
            {
                "title": "test_post_updated",
                "content": "test_content_updated",
                "date_posted": timezone.now(),
                "author": self.user.id,
            },
        )

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Post.objects.first().title, "test_post_updated")
        self.assertEquals(Post.objects.count(), 1)

    def test_post_delete_DELETE(self):
        response = self.client.delete(self.post_delete_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Post.objects.count(), 0)
