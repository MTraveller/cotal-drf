from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from core.do_permissions import do_permissions
from core.models import User
from .serializers import *
from .models import *


class FollowViewSet(ModelViewSet):
    """
    Follow view set with appropiate permission handling.
    """
    serializer_class = FollowSerializer

    def get_permissions(self):
        queryset = Followed.objects \
            .filter(
                followed_by_id=self.request.user.id  # type: ignore
            )
        self.__dict__['queryset'] = list(queryset)
        return do_permissions(self)

    def get_queryset(self):
        return Followed.objects \
            .filter(profile_id=self.kwargs['profiles_pk'])

    def get_serializer_context(self):
        following_by_name = User.objects \
            .get(id=self.kwargs['profiles_pk'])
        return {
            'profile_id': self.kwargs['profiles_pk'],
            'followed_by_id': self.request.user.id,  # type: ignore
            'followed_by_name': self.request.user,
            'followed_by_username': self.request.user.username,  # type: ignore
            'following_by_name': following_by_name,
            'following_by_username': following_by_name.username,
        }


class FollowingViewSet(ModelViewSet):
    """
    Connecting view set with appropiate permission handling.
    """
    serializer_class = FollowingSerializer

    def get_permissions(self):
        queryset = Followed.objects \
            .filter(followed_by_id=self.request.user.id)  # type: ignore
        self.__dict__['queryset'] = list(queryset)
        return do_permissions(self)

    def get_queryset(self):
        return Followed.objects \
            .filter(followed_by_id=self.request.user.id)  # type: ignore
