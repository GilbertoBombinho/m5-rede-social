from rest_framework.views import Request, Response
from .models import Post, PostLike
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import PostSerializer
from .permissions import IsAccountOwner
from rest_framework import generics
from .serializers import LikeSerializer


class PostView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(privacy=False)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_url_kwarg = "pk"


class LikeView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = LikeSerializer
    queryset = PostLike.objects.all()

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.request.data["post_id"])
        return serializer.save(user_like=self.request.user, post=post)


class LikeDestroyView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = PostLike.objects.all()
    serializer_class = LikeSerializer
    lookup_url_kwarg = "pk"
