from rest_framework import serializers

from .models import Follower
from users.models import UserFollower


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ["id", "name"]

    def create(self, validated_data: dict) -> Follower:
        return Follower.objects.create(**validated_data)


class FolloewerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollower
        fields = "__all__"

    def create(self, validated_data: dict) -> Follower:
        return UserFollower.objects.create(**validated_data)
