from rest_framework.viewsets import ModelViewSet
from core.do_permissions import do_permissions
from .serializers import *
from .models import *


class ConnecterViewSet(ModelViewSet):
    """
    Connecter view set with appropiate permission handling.
    To initiate a connection to chosen user.
    """
    serializer_class = ConnecterSerializer

    def get_permissions(self):
        user = Profile.objects \
                      .filter(slug=self.kwargs['profiles_slug'])

        queryset = Connected.objects \
                            .filter(connecting_id=list(user)[0].id)  # type: ignore

        self.__dict__['queryset'] = list(queryset)
        return do_permissions(self)

    def get_queryset(self):
        user_slug = self.kwargs['profiles_slug']

        user = Profile.objects \
                      .filter(slug=user_slug)

        if user_slug == self.request.user.username:  # type: ignore
            return Connected.objects \
                            .filter(connecter_id=self.request.user.id)  # type: ignore

        return Connected.objects \
                        .filter(connecting_id=list(user)[0].id)  # type: ignore

    def get_serializer_context(self):
        user = Profile.objects \
                      .filter(slug=self.kwargs['profiles_slug'])

        return {
            'connecter_id': self.request.user.id,  # type: ignore
            'connecting_id': list(user)[0].id,  # type: ignore
            'connecter_username': self.request.user.username,  # type: ignore
        }


class ConnectingViewSet(ModelViewSet):
    """
    Connecting view set with appropiate permission handling.
    To get all initiated connecting to user.
    """
    serializer_class = ConnectingSerializer

    def get_permissions(self):
        user = Profile.objects \
                      .filter(slug=self.kwargs['profiles_slug'])

        queryset = Connected.objects \
                            .filter(connecting_id=list(user)[0].id)  # type: ignore

        self.__dict__['queryset'] = list(queryset)
        return do_permissions(self)

    def get_queryset(self):
        user = Profile.objects \
                      .filter(slug=self.kwargs['profiles_slug'])

        return Connected.objects \
                        .filter(connecting_id=list(user)[0].id)  # type: ignore
