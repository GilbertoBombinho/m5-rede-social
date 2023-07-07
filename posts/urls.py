from django.urls import path

from . import views
#from songs import views as song_views

urlpatterns = [
    path("posts/", views.PostView.as_view()),
    path("posts/<int:pk>/", views.PostDetailView.as_view()),
   # path("albums/<int:pk>/songs/", song_views.SongView.as_view()),
]