from rest_framework import serializers
from .models import Follower
from users.models import UserFollower
from rest_framework.validators import UniqueValidator


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ["id", "name"]

    def create(self, validated_data: dict) -> Follower:
        return Follower.objects.create(**validated_data)


class FolloewerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollower
        fields = ["follower", "user", "is_friend"]
        read_only_fields = ["follower", "user"]
