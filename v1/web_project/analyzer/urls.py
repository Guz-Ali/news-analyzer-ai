from django.urls import path
from .views import (
    AnalysisCreateView,
    AnalysisDetailView,
    UserAnalysisListView,
    AnalysisDeleteView,
    publishAsPost,
)


urlpatterns = [
    path("analyzer/", AnalysisCreateView.as_view(), name="analyzer-home"),
    path(
        "user/<str:username>/analyses/",
        UserAnalysisListView.as_view(),
        name="user-analyses",
    ),
    path("analysis/<int:pk>/", AnalysisDetailView.as_view(), name="analysis-detail"),
    path(
        "analysis/<int:pk>/delete/",
        AnalysisDeleteView.as_view(),
        name="analysis-delete",
    ),
    path(
        "analysis/<int:pk>/publish/",
        publishAsPost,
        name="analysis-publish",
    ),
]
