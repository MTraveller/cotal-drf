from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from core.do_permissions import do_permissions
from .serializers import *
from .models import *


class ConnecterViewSet(ModelViewSet):
    """
    Profile view set with appropiate permission handling.
    """
    serializer_class = ConnecterSerializer

    def get_permissions(self):
        queryset = Connected.objects \
            .filter(
                # https://docs.djangoproject.com/en/4.1/ref/models/querysets/#or
                Q(connecter_id=self.request.user.id) |  # type: ignore
                Q(connecting_id=self.request.user.id)  # type: ignore
            )
        self.__dict__['queryset'] = list(queryset)
        return do_permissions(self)

    def get_queryset(self):
        return Connected.objects \
            .filter(
                Q(connecter_id=self.request.user.id) |  # type: ignore
                Q(connecting_id=self.request.user.id)  # type: ignore
            )

    def get_serializer_context(self):
        return {
            'connecter_id': self.request.user.id,  # type: ignore
            'connecting_id': self.kwargs['profiles_pk']
        }


class ConnectingViewSet(ModelViewSet):
    """
    Profile view set with appropiate permission handling.
    """
    serializer_class = ConnectingSerializer

    def get_permissions(self):
        queryset = Connected.objects \
            .filter(connecting_id=self.request.user.id)  # type: ignore
        self.__dict__['queryset'] = list(queryset)
        return do_permissions(self)

    def get_queryset(self):
        return Connected.objects \
            .filter(connecting_id=self.request.user.id)  # type: ignore
