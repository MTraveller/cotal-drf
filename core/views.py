from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAuthenticated, DjangoModelPermissions)
from .permissions import IsObjectUser, IsNotObjectUserOrReadOnly
from .models import *
from .serializers import *


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
    elif self.request.resolver_match.url_name == 'profile-me':
        return [IsAuthenticated()]
    elif self.request.resolver_match.url_name == 'profile-detail':
        return [IsNotObjectUserOrReadOnly()]
    return [DjangoModelPermissions()]


class ProfileViewSet(ModelViewSet):
    """
    Profile view set with appropiate permission handling.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        return do_permissions(self)

    # https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing
    @action(detail=False, methods=['GET', 'PUT', 'DELETE'])
    # Add djoser's /me endpoint to /profile endpoint
    def me(self, request):
        if request.user.id:
            profile = Profile.objects\
                .get(id=request.user.id)
            if request.method == 'GET':
                serializer = ProfileSerializer(profile)
                return Response(serializer.data)
            elif request.method == 'PUT':
                serializer = ProfileSerializer(profile, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)
        return Response({
            "detail": "Authentication credentials were not provided."
        })


class LinkViewSet(ModelViewSet):
    """
    Profile link view set with appropiate permission handling.
    """
    serializer_class = ProfileLinktreeSerializer

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        return Linktree.objects.filter(profile_id=self.kwargs['profile_pk'])

    def get_serializer_context(self):
        return {'profile_id': self.kwargs['profile_pk']}


class SocialViewSet(ModelViewSet):
    """
    Profile social view set with appropiate permission handling.
    """
    serializer_class = ProfileSocialSerializer

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        return Social.objects.filter(profile_id=self.kwargs['profile_pk'])

    def get_serializer_context(self):
        return {'profile_id': self.kwargs['profile_pk']}


class PortfolioViewSet(ModelViewSet):
    """
    Profile social view set with appropiate permission handling.
    """
    serializer_class = ProfilePortfolioSerializer

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        return Portfolio.objects.filter(profile_id=self.kwargs['profile_pk'])

    def get_serializer_context(self):
        return {'profile_id': self.kwargs['profile_pk']}


class AwardViewSet(ModelViewSet):
    """
    Profile social view set with appropiate permission handling.
    """
    serializer_class = ProfileAwardSerializer

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        return Award.objects.filter(profile_id=self.kwargs['profile_pk'])

    def get_serializer_context(self):
        return {'profile_id': self.kwargs['profile_pk']}


class CertificateViewSet(ModelViewSet):
    """
    Profile Certificate view set with appropiate permission handling.
    """
    serializer_class = ProfileCertificateSerializer

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        return Certificate.objects.filter(profile_id=self.kwargs['profile_pk'])

    def get_serializer_context(self):
        return {'profile_id': self.kwargs['profile_pk']}


class CreativeViewSet(ModelViewSet):
    """
    Profile Creative view set with appropiate permission handling.
    """
    serializer_class = ProfileCreativeSerializer

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        return Creative.objects.filter(profile_id=self.kwargs['profile_pk'])

    def get_serializer_context(self):
        return {'profile_id': self.kwargs['profile_pk']}


class SettingViewSet(ModelViewSet):
    """
    Profile Setting view set with appropiate permission handling.
    """
    serializer_class = ProfileSettingSerializer

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        return Setting.objects.filter(profile_id=self.kwargs['profile_pk'])

    def get_serializer_context(self):
        return {'profile_id': self.kwargs['profile_pk']}
