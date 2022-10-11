from rest_framework.permissions import (
    IsAuthenticated, DjangoModelPermissions)
from .permissions import IsObjectUser, IsNotObjectUserOrReadOnly


def try_match(self):
    """
    Function to get user id and check against request user id.
    """
    basename = self.request.resolver_match.url_name
    kwargs = self.request.resolver_match.kwargs

    if self.request.user.is_authenticated:
        profile_id = 0
        match basename:
            case 'profile-posts-list':
                profile_id = kwargs['profile_pk']
            case 'profile-posts-detail':
                profile_id = kwargs['profile_pk']
            case 'post-comments-list':
                if self.request.user and self.request.user.is_authenticated:
                    return [IsAuthenticated()]
                else:
                    return False
            case 'post-comments-detail':
                profile_id = self.__dict__['comment_profile_id'].profile_id

        try:
            return bool(self.request.user.id == int(profile_id))
        except KeyError:
            return False

    return False


def do_permissions(self):
    """
    Function to get the appropiate permission.
    """
    url_name = self.request.resolver_match.url_name
    if try_match(self):
        return [IsObjectUser()]
    elif not self.request.user.is_authenticated:
        return [IsNotObjectUserOrReadOnly()]
    return [DjangoModelPermissions()]
