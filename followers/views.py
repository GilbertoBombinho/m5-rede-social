from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from serializer import FollowerSerializer, FolloewerUserSerializer
from models import Follower
from users.models import User, UserFollower

# from users.serializer import UserSerializer


class FollowerView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer


class UnfollowerView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer


class FollowUserView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FolloewerUserSerializer

    def perform_create(self, serializer):
        follower = self.request.user
        user_to_follow_id = self.request.data.get("user_id")
        user_to_follow = User.objects.get(id=user_to_follow_id)

        serializer.save(follower=follower, user=user_to_follow, is_friend=True)
