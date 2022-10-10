from rest_framework.permissions import (
    IsAuthenticated, DjangoModelPermissions)
from .permissions import IsObjectUser, IsNotObjectUserOrReadOnly


def try_match(self):
    """
    Function to get user id and check against request user id.
    """
    kwargs = self.request.resolver_match.kwargs
    value = dict((value, key)
                 for key, value in kwargs
                 .items()).get(str(self.request.user.id))
    try:
        return bool(self.request.user.id == int(kwargs[value]))
    except KeyError:
        return False


def do_permissions(self):
    """
    Function to get the appropiate permission.
    """
    if try_match(self):
        return [IsObjectUser()]
    elif self.request.resolver_match.url_name == 'profile-me' \
            or self.request.resolver_match.url_name == 'post-comments-list':
        return [IsAuthenticated()]
    elif self.request.resolver_match.url_name == 'profile-detail':
        return [IsNotObjectUserOrReadOnly()]
    return [DjangoModelPermissions()]
