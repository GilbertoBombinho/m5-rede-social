from django.db import models
from django.contrib.auth.models import AbstractUser
from followers.models import Follower


class User(AbstractUser):
    email = models.EmailField(unique=True)
    followers = models.ManyToManyField(
        "followers.Follower", through="users.UserFollower", related_name="user_follower"
    )


class UserFollower(models.Model):
    follower = models.ForeignKey(
        "followers.Follower", on_delete=models.CASCADE, related_name="followers"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_name_follower"
    )
<<<<<<< HEAD
    is_friend = models.BooleanField(default=False)
=======
>>>>>>> 5444ba430684fb4c80985fa497292cdcb4891f86
