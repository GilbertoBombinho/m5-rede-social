from rest_framework import serializers
from .models import Post, PostLike
from comments.serializers import CommentSerializer


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ["id", "status", "user_like_id", "post_id"]

        def create(self, validated_data: dict) -> PostLike:
            return PostLike.objects.create(**validated_data)


class PostSerializer(serializers.ModelSerializer):
    posts_comment = CommentSerializer(many=True, read_only=True)
    # post_like = LikeSerializer(many=True, read_only=True)
    likes_count = serializers.ReadOnlyField(source="post_like.count")

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "privacy",
            "user_id",
            "likes_count",
            "posts_comment",
        ]
