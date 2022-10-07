from rest_framework.viewsets import ModelViewSet
from core.do_permissions import do_permissions
from .models import *
from .serializers import *


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
