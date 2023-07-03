from rest_framework import serializers

from models import Follower

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ['id','name']

    def create(self, validated_data: dict) -> Follower:
        return Follower.objects.create(**validated_data)