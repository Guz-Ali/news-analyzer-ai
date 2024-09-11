from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Analysis


# def home(request):
#     return render(request, "analyzer/analysis.html")


class AnalysisCreateView(LoginRequiredMixin, CreateView):
    model = Analysis
    fields = ["title", "keywords", "prompt", "date_range_start", "date_range_end"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
