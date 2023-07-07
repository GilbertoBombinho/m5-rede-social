from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
from users.models import User


class Like(models.Model):
    status = models.BooleanField(default=False)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="users_like"
    )
>>>>>>> 50bacb5ccb1653649d27df2c9f5a1a1d2e63dcfc
