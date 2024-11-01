from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Post
from django.utils import timezone
from django.urls import reverse


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="em@gmail.com", password="password"
        )

    def test_model_Post(self):
        post = Post.objects.create(
            title="test_post",
            content="test_content",
            date_posted=timezone.now(),
            author=self.user,
            is_public=True,
        )

        self.assertEquals(str(post), "test_post")
        self.assertTrue(isinstance(post, Post))


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

        self.post_owned = Post.objects.create(
            title="test_post_2",
            content="test_content_2",
            date_posted=timezone.now(),
            author=self.user_login,
            is_public=True,
        )

        self.post_public = Post.objects.create(
            title="test_post_3",
            content="test_content_2",
            date_posted=timezone.now(),
            author=self.user_other,
            is_public=True,
        )

        self.post_private = Post.objects.create(
            title="test_post_4",
            content="test_content_2",
            date_posted=timezone.now(),
            author=self.user_other,
            is_public=False,
        )

        self.home_url = reverse("blog-home")
        self.post_create_url = reverse("post-create")
        self.post_detail_url = reverse("post-detail", args=[self.post_owned.id])
        self.post_public_detail_url = reverse("post-detail", args=[self.post_public.id])
        self.post_private_detail_url = reverse(
            "post-detail", args=[self.post_private.id]
        )
        self.post_edit_url = reverse("post-update", args=[self.post_owned.id])
        self.post_delete_url = reverse("post-delete", args=[self.post_owned.id])
        self.user_posts_url = reverse("user-posts", args=[self.user_login.username])
        self.user_other_posts_url = reverse(
            "user-posts", args=[self.user_other.username]
        )

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/home.html")

    def test_user_posts_GET(self):
        response = self.client.get(self.user_posts_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/user_posts.html")
        self.assertEquals(
            Post.objects.filter(author=self.user_login.id).count(),
            len(response.context["object_list"]),
        )

    def test_user_other_posts_GET(self):
        response = self.client.get(self.user_other_posts_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/user_posts.html")
        self.assertEquals(
            Post.objects.filter(author=self.user_other.id, is_public=True).count(),
            len(response.context["object_list"]),
        )

    def test_post_detail_GET(self):
        response = self.client.get(self.post_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTrue(isinstance(response.context["object"], Post))

    def test_post_public_detail_GET(self):
        response = self.client.get(self.post_public_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTrue(isinstance(response.context["object"], Post))

    def test_post_private_detail_GET(self):
        response = self.client.get(self.post_private_detail_url)

        self.assertEquals(response.status_code, 404)

    def test_post_create_POST(self):
        response = self.client.post(
            self.post_create_url,
            {
                "title": "test_post_3",
                "content": "test_content_3",
                "date_posted": timezone.now(),
                "author": self.user_login.id,
                "is_public": True,
            },
        )

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Post.objects.count(), 4)
        self.assertEquals(Post.objects.last().title, "test_post_3")

    def test_post_create_POST_no_data(self):
        response = self.client.post(self.post_create_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Post.objects.count(), 3)

    def test_post_edit_POST(self):
        response = self.client.post(
            self.post_edit_url,
            {
                "title": "test_post_updated",
                "content": "test_content_updated",
                "date_posted": timezone.now(),
                "author": self.user_login.id,
                "is_public": True,
            },
        )

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Post.objects.first().title, "test_post_updated")
        self.assertEquals(Post.objects.count(), 3)

    def test_post_delete_DELETE(self):
        response = self.client.delete(self.post_delete_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Post.objects.count(), 2)
