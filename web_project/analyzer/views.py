from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
)
from .models import Analysis
from .tasks import createPostFromAnalysis
from blog.models import Post


class AnalysisCreateView(LoginRequiredMixin, CreateView):
    model = Analysis
    fields = ["title", "keywords", "prompt", "date_range_start", "date_range_end"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AnalysisDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Analysis

    def test_func(self):
        analysis = self.get_object()
        return self.request.user == analysis.author


class UserAnalysisListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Analysis
    template_name = "analyzer/user_analyses.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "analyses"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Analysis.objects.filter(author=user).order_by("-date_posted")

    def test_func(self):
        analysis = self.get_queryset().first()
        return self.request.user == analysis.author


class AnalysisDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Analysis
    success_url = "/"

    def test_func(self):
        analysis = self.get_object()
        return self.request.user == analysis.author


@login_required
def publishAsPost(request, *args, **kwargs):
    analysis = Analysis.objects.get(id=kwargs.get("pk"))
    if request.method != "POST" or request.user != analysis.author:
        return render(request, "analyzer/analysis_detail.html", {"object": analysis})

    try:
        post = Post.objects.get(analysis=analysis)
    except:
        post = createPostFromAnalysis(analysis)
    post.is_public = True
    post.save()
    return render(request, "blog/post_detail.html", {"object": post})
