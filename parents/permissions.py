from rest_framework.permissions import BasePermission


class IsParent(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'parent')
