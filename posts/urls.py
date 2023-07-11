from django.urls import path
from . import views


urlpatterns = [
    path("posts/", views.PostView.as_view()),
    path("posts/list", views.PostListView.as_view()),
    path("posts/<int:pk>", views.PostDetailView.as_view()),
]
