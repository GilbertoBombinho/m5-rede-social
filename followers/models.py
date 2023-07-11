from django.db import models


class Follower(models.Model):
    name = models.CharField(max_length=50, null=True, unique=True)
