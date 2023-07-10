from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from django.contrib.auth.hashers import make_password
from posts.serializers import PostSerializer


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    users_post = PostSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ["id", "email", "password", "username", "first_name", "last_name", "users_post"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        new_password = validated_data.get("password")
        if new_password:
            instance.password = make_password(new_password)

        instance.save()

        return instance
