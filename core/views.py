from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .do_permissions import do_permissions
from .serializers import *
from .models import *


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
