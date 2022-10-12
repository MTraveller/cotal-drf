from rest_framework.permissions import (
    IsAuthenticated, DjangoModelPermissions)
from .permissions import IsObjectUser, IsNotObjectUserOrReadOnly


BASENAME_LIST = [
    'profile-connecter-list',
    'profile-connecting-list',
    'profile-follows-list',
]

BASENAME_DETAIL = [
    'profile-connecter-detail',
    'profile-follows-detail',
]


def try_match(self):
    """
    Function to get user id and check against request user id.
    """
    basename = self.request.resolver_match.url_name
    kwargs = self.request.resolver_match.kwargs

    if self.request.user.is_authenticated:
        profile_id = 0
        if basename == 'profile-me':
            return [IsAuthenticated()]

        if basename in BASENAME_LIST:
            if not len(self.queryset) >= 1 \
                and not \
                    int(kwargs['profiles_pk']) == self.request.user.id:
                return [IsAuthenticated()]
            return False

        elif basename in BASENAME_DETAIL:
            try:
                queryset_dict = self.queryset[0].__dict__
                if 'connecter_id' in queryset_dict and \
                        queryset_dict['connecter_id'] == self.request.user.id or \
                        queryset_dict['followed_id'] == self.request.user.id:
                    return [IsAuthenticated()]
            except IndexError:
                pass

            return False

        if basename.startswith('profile-'):
            if 'profiles_pk' in kwargs:
                profile_id = kwargs['profiles_pk']
            elif 'pk' in kwargs:
                profile_id = kwargs['pk']

        elif basename.startswith('posts-') or \
                basename.startswith('post-'):
            match basename:
                case 'posts-list':
                    profile_id = kwargs['profile_pk']
                case 'posts-detail':
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
    if try_match(self):
        return [IsObjectUser()]
    elif not self.request.user.is_authenticated:
        return [IsNotObjectUserOrReadOnly()]
    return [DjangoModelPermissions()]
