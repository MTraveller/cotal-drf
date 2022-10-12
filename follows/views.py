from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from core.do_permissions import do_permissions
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
                followed_id=self.request.user.id  # type: ignore
            )
        self.__dict__['queryset'] = list(queryset)
        return do_permissions(self)

    def get_queryset(self):
        return Followed.objects \
            .filter(profile_id=self.kwargs['profiles_pk'])

    def get_serializer_context(self):
        return {
            'profile_id': self.kwargs['profiles_pk'],
            'followed_id': self.request.user.id,  # type: ignore
            'following_id': self.kwargs['profiles_pk']
        }
