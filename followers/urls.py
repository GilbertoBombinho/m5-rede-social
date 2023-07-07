from django.urls import path
from . import views

urlpatterns = [
    path("follower/", views.FollowerView.as_view()),
    path("unfollower/<int:pk>/", views.UnfollowerView.as_view()),
    path("followeruser/", views.FollowUserView.as_view()),
]
