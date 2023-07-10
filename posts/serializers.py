from rest_framework import serializers
from .models import Post
from comments.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    posts_comment = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ["id", "title", "content", "privacy","user_id", "like_id", "posts_comment"]

        
        