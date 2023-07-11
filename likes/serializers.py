from rest_framework import serializers
from .models import Like
from posts.models import PostLike


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["id", "status", "user_id"]

        def create(self, validated_data: dict) -> Like:
            return Like.objects.create(**validated_data)


class FolloewerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ["like", "post", "status"]
        read_only_fields = ["like", "post"]
