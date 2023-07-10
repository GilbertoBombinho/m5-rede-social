from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Comment,Post,User

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = [
            "id",
            "content",
            "post",
            "user",
        ]

        extra_kwargs = {'user': {'read_only': True}}
    
    