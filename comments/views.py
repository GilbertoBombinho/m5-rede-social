from rest_framework import generics,permissions
from rest_framework.generics import ListAPIView
from users.permission import IsAccountOwner
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication

class CommentCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be authenticated to create a comment.")
        serializer.save(user=self.request.user)

class CommentUpdateView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    

class CommentDeleteView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    
