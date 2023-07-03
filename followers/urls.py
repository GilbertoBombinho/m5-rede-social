from django.urls import path
from views import FollowerView

urlpatterns = [
    path('follower/',FollowerView.as_view()),
]