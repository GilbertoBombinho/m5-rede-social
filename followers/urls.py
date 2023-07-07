from django.urls import path
from views import FollowerView, UnfollowerView, FollowUserView

urlpatterns = [
    path("follower/", FollowerView.as_view()),
    path("unfollower/", UnfollowerView.as_view()),
    path("followeruser/", FollowUserView.as_view()),
]
