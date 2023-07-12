from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=None)
    privacy = models.BooleanField(default=False)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="users_post"
    )


class PostLike(models.Model):
    post = models.ForeignKey(
        "posts.Post", on_delete=models.CASCADE, related_name="post_like"
    )
    user_like = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="users_like"
    )
    status = models.BooleanField(default=False)
