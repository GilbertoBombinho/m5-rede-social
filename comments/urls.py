from django.urls import path
from .views import (
    CommentCreateView,
    CommentListView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    path("comments/", CommentListView.as_view(), name="comment_list"),
    path("comments/create/", CommentCreateView.as_view(), name="comment_create"),
    path(
        "comments/<int:pk>/update/", CommentUpdateView.as_view(), name="comment_update"
    ),
    path(
        "comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"
    ),
]
