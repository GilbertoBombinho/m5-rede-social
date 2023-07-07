from django.db import models
from likes.models import Like
from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=None)
    privacy = models.BooleanField(default=False)
    like = models.ForeignKey(
        "likes.Like", on_delete=models.CASCADE, related_name="likes_post", null=True
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="users_post"
    )

