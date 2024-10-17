from rest_framework import permissions

class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True  # Allow read access to everyone
        return obj.author == request.user  # Allow delete access only to the author
