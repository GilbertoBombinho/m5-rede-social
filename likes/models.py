from django.db import models

from users.models import User





class Like(models.Model):
    status = models.BooleanField(default=False)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="users_like"
    )

