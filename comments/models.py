from django.db import models
from users.models import User
from posts.models import Post


class Comment(models.Model):
    content = models.TextField(max_length=None)
    post = models.ForeignKey(
        "posts.Post", on_delete=models.CASCADE, related_name="posts_comment"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="users_comment"
    )
