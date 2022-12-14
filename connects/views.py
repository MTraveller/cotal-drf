from django.http import Http404
from django.db.models import Q
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
        try:
            queryset = Connected.objects \
                                .filter(
                                    Q(connecter_id=list(user)[0].id) |
                                    Q(connecting_id=list(user)[0].id)
                                )
            has_object = False
            for obj in list(queryset):
                if obj.connecter_id == self.request.user.id or \
                        obj.connecting_id == self.request.user.id:  # type: ignore
                    has_object = True

            self.__dict__['has_object'] = has_object
            self.__dict__['queryset'] = list(queryset)

        except:
            pass

        return do_permissions(self)

    def get_queryset(self):
        user_slug = self.kwargs['profiles_slug']

        user = Profile.objects \
                      .filter(slug=user_slug)

        if user_slug == self.request.user.username:  # type: ignore
            return Connected.objects \
                            .filter(connecter_id=self.request.user.id)  # type: ignore
        try:
            return Connected.objects \
                            .filter(connecting_id=list(user)[0].id)  # type: ignore
        except:
            raise Http404

    def get_serializer_context(self):
        user = Profile.objects \
                      .filter(slug=self.kwargs['profiles_slug'])
        try:
            return {
                'connecter_id': self.request.user.id,  # type: ignore
                'connecting_id': list(user)[0].id,  # type: ignore
                'connecter_username': self.request.user.username,  # type: ignore
            }
        except:
            raise Http404


class ConnectingViewSet(ModelViewSet):
    """
    Connecting view set with appropiate permission handling.
    To get all initiated connections to user.
    """
    serializer_class = ConnectingSerializer

    def get_permissions(self):
        user = Profile.objects \
                      .filter(slug=self.kwargs['profiles_slug'])
        try:
            queryset = Connected.objects \
                                .filter(connecting_id=list(user)[0].id)  # type: ignore

            self.__dict__['queryset'] = list(queryset)
        except:
            pass

        return do_permissions(self)

    def get_queryset(self):
        user = Profile.objects \
                      .filter(slug=self.kwargs['profiles_slug'])

        try:
            return Connected.objects \
                            .filter(
                                Q(connecter_id=list(user)[0].id) |
                                Q(connecting_id=list(user)[0].id)
                            )
        except:
            raise Http404

    def get_serializer_context(self):
        return {"request_user_id": self.request.user.id}  # type: ignore
