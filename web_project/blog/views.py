from django.shortcuts import render
from .models import Post

posts = [
    {
        "author": "Ali",
        "title": "blog post 1",
        "content": "first post content",
        "date_posted": "August 1, 2024",
    },
    {
        "author": "Veli",
        "title": "blog post 2",
        "content": "seoncd post content",
        "date_posted": "August 2, 2024",
    },
    {
        "author": "Deli",
        "title": "blog post 3",
        "content": "third post content",
        "date_posted": "August 3, 2024",
    },
]


def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
