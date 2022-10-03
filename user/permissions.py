from rest_framework import permissions


class IsObjectUser(permissions.BasePermission):
    """
    Overwrite default rest_framework BasePermission
    """

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True

    # Overwrite rest_framework > permissions.py > BasePermission > has_object_permission
    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if request.user and request.user.id == obj.id:
            return True
        return IsObjectUser.has_permission
