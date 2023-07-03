from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
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

>>>>>>> 50bacb5ccb1653649d27df2c9f5a1a1d2e63dcfc
