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
    'profile-connecting-detail',
    'profile-follows-detail',
]


def try_match(self):
    """
    Function to get user id and check against request user id.
    """
    basename = self.request.resolver_match.url_name
    kwargs = self.request.resolver_match.kwargs

    if self.request.user.is_authenticated:
        profile_id = False
        profile_slug = False
        if basename == 'profile-me':
            return [IsAuthenticated()]

        if basename in BASENAME_LIST:
            if basename == 'profile-connecter-list':
                if not self.has_object == True:
                    if not kwargs['profiles_slug'] \
                            == self.request.user.profile.slug:
                        return [IsAuthenticated()]

                    elif not len(self.queryset) >= 1 \
                        and not \
                            (kwargs[
                                'profiles_slug'
                            ]) == self.request.user.profile.slug:
                        if basename == 'profile-connecting-list' and \
                                len(self.queryset) == 0:
                            return False

                        return [IsAuthenticated()]

            return False

        elif basename in BASENAME_DETAIL:
            try:
                queryset_dict = self.queryset[0].__dict__

                if basename == 'profile-connecter-detail' and \
                    'connecter_id' in queryset_dict and \
                        queryset_dict['connecter_id'] == self.request.user.id:

                    return [IsAuthenticated()]

                elif basename == 'profile-connecting-detail' and \
                    'connecting_id' in queryset_dict and \
                        queryset_dict[
                            'connecting_id'
                        ] == self.request.user.id:
                    return [IsAuthenticated()]

            except IndexError:
                pass

            return False

        if basename.startswith('profile-'):
            if 'profiles_slug' in kwargs:
                profile_slug = kwargs['profiles_slug']
            elif 'pk' in kwargs:
                profile_slug = kwargs['pk']

        elif basename.startswith('posts-') or \
                basename.startswith('post-'):
            match basename:
                case 'posts-list' | 'posts-detail':
                    profile_slug = kwargs['profile_slug']
                case 'post-comments-list':
                    if self.request.user \
                            and self.request.user.is_authenticated:
                        return [IsAuthenticated()]
                    else:
                        return False
                case 'post-comments-detail':
                    profile_id = self.__dict__['comment_profile_id'] \
                        .profile_id

        try:

            return bool(
                self.request.user.username.lower() == profile_slug
                if profile_slug else self.request.user.id
                == profile_id if profile_id else False
            )

        except KeyError:
            return False

    return False


def do_permissions(self):
    """
    Function to get the appropiate permission.
    """
    if try_match(self):
        print("True - TRY_MATCH")
        return [IsObjectUser()]
    elif not self.request.user.is_authenticated:
        return [IsNotObjectUserOrReadOnly()]
    return [DjangoModelPermissions()]
