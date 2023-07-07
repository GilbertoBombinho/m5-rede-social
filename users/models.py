from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from followers.models import Follower


class User(AbstractUser):
    user_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(unique=True)
    followers = models.ManyToManyField("followers.Follower", through="users.UserFollower", related_name="user_follower")


class UserFollower(models.Model):
    follower = models.ForeignKey("followers.Follower", on_delete=models.CASCADE, related_name="followers")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_name_follower")
