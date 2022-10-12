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
            .filter(connecter_id=self.request.user.id)  # type: ignore
        self.__dict__['queryset'] = list(queryset)
        return do_permissions(self)

    def get_queryset(self):
        return Connected.objects \
            .filter(connecting_id=self.kwargs['profiles_pk'])

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
        return do_permissions(self)

    def get_queryset(self):
        return Connected.objects \
            .filter(connecting_id=self.request.user.id)  # type: ignore

    def get_serializer_context(self):
        basename = self.request.resolver_match.url_name
        print(self.kwargs)
        if basename == 'profile-connecting-detail':
            return {
                'id': self.kwargs['pk'],
                'connecting_id': self.kwargs['profiles_pk']
            }
        return {
            'connecting_id': self.kwargs['profiles_pk']
        }
