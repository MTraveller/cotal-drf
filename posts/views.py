from django.db.models import Prefetch
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.do_permissions import do_permissions
from profiles.models import Profile
from .models import *
from .serializers import *


class ProfilePostViewSet(ModelViewSet):
    """
    Profile post view set with appropiate permission handling.
    """
    # https://docs.djangoproject.com/en/4.1/ref/models/querysets/#django.db.models.Prefetch
    queryset = Profile.objects \
        .select_related('user') \
        .prefetch_related('posts') \
        .prefetch_related(Prefetch('posts__postimages')) \
        .prefetch_related(Prefetch('posts__postcomments')) \
        .all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        return do_permissions(self)


class PostViewSet(ModelViewSet):
    """
    Post view set with appropiate permission handling.
    """
    serializer_class = PostSerializer

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        return Post.objects \
            .prefetch_related('postimages') \
            .prefetch_related('postcomments') \
            .filter(profile_id=self.kwargs['profiles_pk'])

    def get_serializer_context(self):
        return {'profile_id': self.kwargs['profiles_pk']}


class PostImageViewSet(ModelViewSet):
    """
    Post image view set with appropiate permission handling.
    """
    serializer_class = PostImageSerializer

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        return PostImage.objects \
            .filter(profile_id=self.kwargs['profiles_pk'])

    def get_extra_context(self):
        return {'profile_id': self.kwargs['profiles_pk']}


class PostCommentViewSet(ModelViewSet):
    """
    Post comment view set with appropiate permission handling.
    """
    serializer_class = PostCommentSerializer

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        return PostComment.objects \
            .select_related('profile') \
            .filter(profile_id=self.kwargs['profiles_pk'])

    def get_extra_context(self):
        return {'profile_id': self.kwargs['profiles_pk']}
