from rest_framework import permissions
from rest_framework.permissions import BasePermission


class AdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or (
            request.method in permissions.SAFE_METHODS)
