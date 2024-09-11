from django.urls import path
from .views import AnalysisCreateView
from . import views


urlpatterns = [
    # path("analyzer/", views.home, name="analyzer-home"),
    path("analyzer/", AnalysisCreateView.as_view(), name="analysis-home"),
    # path("about/", views.about, name="blog-about"),
]
