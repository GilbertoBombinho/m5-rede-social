from rest_framework import permissions
from .models import Post
from rest_framework.views import View, Request


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Post) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and obj.user == request.user
