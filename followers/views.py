
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from serializer import FollowerSerializer
from models import Follower

# Create your views here.
class FollowerView(generics.CreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer