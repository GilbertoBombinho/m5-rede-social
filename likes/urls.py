from django.urls import path
from . import views


urlpatterns = [
    path("like/", views.LikeView.as_view()),
    path("like/<int:pk>/", views.LikeDestroyView.as_view()),
]
