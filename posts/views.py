from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.do_permissions import do_permissions
from profiles.models import Profile
from .models import *
from .serializers import *


class ProfileViewSet(ModelViewSet):
    """
    Profile view set with appropiate permission handling.
    """
    queryset = Profile.objects \
        .prefetch_related('user') \
        .prefetch_related('posts') \
        .prefetch_related('postimages') \
        .prefetch_related('postcomments') \
        .all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        return do_permissions(self)


class PostViewSet(ModelViewSet):
    """
    Profile post view set with appropiate permission handling.
    """
    serializer_class = PostSerializer

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        return Post.objects.filter(profile_id=self.kwargs['profiles_pk'])

    def get_serializer_context(self):
        return {'profile_id': self.kwargs['profiles_pk']}
