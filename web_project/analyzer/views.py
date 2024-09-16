from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
)
from .models import Analysis


class AnalysisCreateView(LoginRequiredMixin, CreateView):
    model = Analysis
    fields = ["title", "keywords", "prompt", "date_range_start", "date_range_end"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AnalysisDetailView(DetailView):
    model = Analysis


class UserAnalysisListView(ListView):
    model = Analysis
    template_name = "analyzer/user_analyses.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "analyses"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Analysis.objects.filter(author=user).order_by("-date_posted")


class AnalysisDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Analysis
    success_url = "/"

    def test_func(self):
        analysis = self.get_object()
        return self.request.user == analysis.author
