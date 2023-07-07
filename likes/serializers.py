from rest_framework import serializers
from .models import Like


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["id", "status", "user_id"]