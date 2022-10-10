from rest_framework.permissions import (
    IsAuthenticated, DjangoModelPermissions)

from posts.models import PostComment
from .permissions import IsObjectUser, IsNotObjectUserOrReadOnly


def try_match(self):
    """
    Function to get user id and check against request user id.
    """
    basename = self.request.resolver_match.url_name
    kwargs = self.request.resolver_match.kwargs
    # print(kwargs)
    # print(len(kwargs))
    # for key, val in kwargs.items():
    #     if len(kwargs) <= 2:
    #         if key == 'profile_pk':
    #             profile_pk = val
    #             break
    #     else:
    #         if key == 'pk':
    #             pk = val
    #             break

    print(basename)
    if self.request.user.is_authenticated:
        profile_id = 0
        match basename:
            case 'profile-posts-list':
                profile_id = kwargs['profile_pk']
            case 'profile-posts-detail':
                profile_id = kwargs['profile_pk']
            case 'post-comments-list':
                print(basename)
                if self.request.user and self.request.user.is_authenticated:
                    return [IsAuthenticated()]
                else:
                    return False
            case 'post-comments-detail':
                pk = kwargs['pk']
                profile_id = PostComment.objects.get(id=pk).profile_id

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
    elif url_name == 'profile-me':
        return [IsAuthenticated()]
    elif url_name == 'profile-detail' \
            or url_name == 'profile-posts-detail' \
            or url_name == 'post-comments-list' \
            or url_name == 'post-comments-detail':
        return [IsNotObjectUserOrReadOnly()]
    return [DjangoModelPermissions()]
