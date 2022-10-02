from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .models import Profile, Link, Social
from .serializers import ProfileSerializer, ProfileLinkSerializer, ProfileSocialSerializer


class ProfileViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class LinkViewSet(ModelViewSet):
    serializer_class = ProfileLinkSerializer

    def get_queryset(self):
        return Link.objects.filter(profile_id=self.kwargs['profile_pk'])

    def get_serializer_context(self):
        return {'profile_id': self.kwargs['profile_pk']}


class SocialViewSet(ModelViewSet):
    serializer_class = ProfileSocialSerializer

    def get_queryset(self):
        return Social.objects.filter(profile_id=self.kwargs['profile_pk'])

    def get_serializer_context(self):
        return {'profile_id': self.kwargs['profile_pk']}
