from django.urls import path
from . import views

urlpatterns = [
    path("follower/", views.FollowerView.as_view()),
    path("follower/<int:pk>/", views.UnfollowerView.as_view()),
    path("follower/user/", views.FollowUserView.as_view()),
]
