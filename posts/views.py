from rest_framework.views import Request, Response
from .models import Post
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import PostSerializer
from .permissions import IsAccountOwner
from rest_framework import generics


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
