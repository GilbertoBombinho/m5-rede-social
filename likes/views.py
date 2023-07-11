from rest_framework.views import Request, Response
from .models import Like
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import PostSerializer
from rest_framework import generics


class LikeView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = PostSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class LikeDestroyView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Like.objects.all()
    serializer_class = PostSerializer
    lookup_url_kwarg = "pk"
