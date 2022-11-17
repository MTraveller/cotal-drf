from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.do_permissions import do_permissions
from .models import *
from .serializers import *


class ProfileViewSet(ModelViewSet):
    """
    Profile view set with appropiate permission handling.
    """
    queryset = Profile.objects \
        .prefetch_related(
            'user',
            'linktrees', 'socials',
            'portfolios', 'awards',
            'certificates', 'creatives',
            'settings'
        ) \
        .all()
    serializer_class = ProfileSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        return do_permissions(self)

    # https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing
    @action(detail=False, methods=['GET', 'PUT', 'DELETE'])
    # Add djoser's /me endpoint to /profile endpoint
    def me(self, request):
        if request.user.id:
            # https://docs.djangoproject.com/en/4.1/ref/models/querysets/#or
            profile = Profile.objects \
                .prefetch_related(
                    'user',
                    'linktrees', 'socials',
                    'portfolios', 'awards',
                    'certificates', 'creatives',
                    'settings'
                ) \
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
        user = Profile.objects \
                      .filter(slug=self.kwargs['profiles_slug'])

        return Linktree.objects \
                       .filter(profile_id=list(user)[0].id)  # type: ignore

    def get_serializer_context(self):
        return {'profile_id': self.request.user.id}  # type: ignore


class SocialViewSet(ModelViewSet):
    """
    Profile social view set with appropiate permission handling.
    """
    serializer_class = ProfileSocialSerializer

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        user = Profile.objects \
                      .filter(slug=self.kwargs['profiles_slug'])

        return Social.objects \
                     .filter(profile_id=list(user)[0].id)  # type: ignore

    def get_serializer_context(self):
        return {'profile_id': self.request.user.id}  # type: ignore


class PortfolioViewSet(ModelViewSet):
    """
    Profile social view set with appropiate permission handling.
    """
    serializer_class = ProfilePortfolioSerializer

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        user = Profile.objects \
                      .filter(slug=self.kwargs['profiles_slug'])

        return Portfolio.objects \
                        .filter(profile_id=list(user)[0].id)  # type: ignore

    def get_serializer_context(self):
        return {'profile_id': self.request.user.id}  # type: ignore


class AwardViewSet(ModelViewSet):
    """
    Profile social view set with appropiate permission handling.
    """
    serializer_class = ProfileAwardSerializer

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        user = Profile.objects \
                      .filter(slug=self.kwargs['profiles_slug'])

        return Award.objects \
                    .filter(profile_id=list(user)[0].id)  # type: ignore

    def get_serializer_context(self):
        return {'profile_id': self.request.user.id}  # type: ignore


class CertificateViewSet(ModelViewSet):
    """
    Profile Certificate view set with appropiate permission handling.
    """
    serializer_class = ProfileCertificateSerializer

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        user = Profile.objects \
                      .filter(slug=self.kwargs['profiles_slug'])

        return Certificate.objects \
                          .filter(profile_id=list(user)[0].id)  # type: ignore

    def get_serializer_context(self):
        return {'profile_id': self.request.user.id}  # type: ignore


class CreativeViewSet(ModelViewSet):
    """
    Profile Creative view set with appropiate permission handling.
    """
    serializer_class = ProfileCreativeSerializer

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        user = Profile.objects \
                      .filter(slug=self.kwargs['profiles_slug'])

        return Creative.objects \
                       .filter(profile_id=list(user)[0].id)  # type: ignore

    def get_serializer_context(self):
        return {'profile_id': self.request.user.id}  # type: ignore


class SettingViewSet(ModelViewSet):
    """
    Profile Setting view set with appropiate permission handling.
    """
    serializer_class = ProfileSettingSerializer

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        user = Profile.objects \
                      .filter(slug=self.kwargs['profiles_slug'])

        return Setting.objects \
                      .filter(profile_id=list(user)[0].id)  # type: ignore

    def get_serializer_context(self):
        return {'profile_id': self.request.user.id}  # type: ignore
