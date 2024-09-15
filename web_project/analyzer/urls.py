from django.urls import path
from .views import AnalysisCreateView, AnalysisDetailView, UserAnalysisListView


urlpatterns = [
    path("analyzer/", AnalysisCreateView.as_view(), name="analyzer-home"),
    path("user/<str:username>", UserAnalysisListView.as_view(), name="user-analyses"),
    path("analysis/<int:pk>/", AnalysisDetailView.as_view(), name="analysis-detail"),
]
