from django.http import Http404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.do_permissions import do_permissions
from .models import *
from .serializers import *
from rest_framework.response import Response


class ProfileViewSet(ModelViewSet):
    """
    Profile view set with appropiate permission handling.
    """
    queryset = Profile.objects \
        .prefetch_related('user') \
        .select_related('linktrees', 'socials') \
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
                ) \
                .get(id=request.user.id)

            if request.method == 'GET':
                serializer = ProfileSerializer(profile)
                return Response(serializer.data)

            elif request.method == 'PUT':
                serializer = ProfileSerializer(profile, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        queryset = Profile.objects \
            .filter(slug=self.kwargs['profiles_slug'])
        try:
            return Linktree.objects \
                .filter(profile_id=list(queryset)[0].id)  # type: ignore
        except:
            raise Http404

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
        queryset = Profile.objects \
            .filter(slug=self.kwargs['profiles_slug'])
        try:
            return Social.objects \
                .filter(profile_id=list(queryset)[0].id)  # type: ignore
        except:
            raise Http404

    def get_serializer_context(self):
        return {'profile_id': self.request.user.id}  # type: ignore


class PortfolioViewSet(ModelViewSet):
    """
    Profile social view set with appropiate permission handling.
    """
    serializer_class = ProfilePortfolioSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        queryset = Profile.objects \
            .filter(slug=self.kwargs['profiles_slug'])

        try:
            return Portfolio.objects \
                .filter(profile_id=list(queryset)[0].id)  # type: ignore
        except:
            raise Http404

    def get_serializer_context(self):
        return {'profile_id': self.request.user.id}  # type: ignore


class AwardViewSet(ModelViewSet):
    """
    Profile social view set with appropiate permission handling.
    """
    serializer_class = ProfileAwardSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        queryset = Profile.objects \
            .filter(slug=self.kwargs['profiles_slug'])
        try:
            return Award.objects \
                .filter(profile_id=list(queryset)[0].id)  # type: ignore
        except:
            raise Http404

    def get_serializer_context(self):
        return {'profile_id': self.request.user.id}  # type: ignore


class CertificateViewSet(ModelViewSet):
    """
    Profile Certificate view set with appropiate permission handling.
    """
    serializer_class = ProfileCertificateSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        queryset = Profile.objects \
            .filter(slug=self.kwargs['profiles_slug'])
        try:
            return Certificate.objects \
                .filter(profile_id=list(queryset)[0].id)  # type: ignore
        except:
            raise Http404

    def get_serializer_context(self):
        return {'profile_id': self.request.user.id}  # type: ignore


class CreativeViewSet(ModelViewSet):
    """
    Profile Creative view set with appropiate permission handling.
    """
    serializer_class = ProfileCreativeSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        queryset = Profile.objects \
            .filter(slug=self.kwargs['profiles_slug'])
        try:
            return Creative.objects \
                .filter(profile_id=list(queryset)[0].id)  # type: ignore
        except:
            raise Http404

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
        queryset = Profile.objects \
            .filter(slug=self.kwargs['profiles_slug'])
        try:
            return Setting.objects \
                .filter(profile_id=list(queryset)[0].id)  # type: ignore
        except:
            raise Http404

    def get_serializer_context(self):
        return {'profile_id': self.request.user.id}  # type: ignore
