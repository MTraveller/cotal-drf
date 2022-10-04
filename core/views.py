from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .permissions import IsObjectUser
from .models import Profile, Link, Social
from .serializers import ProfileSerializer, ProfileLinkSerializer, ProfileSocialSerializer


def try_match(self):
    """
    Function to get user id and check against request user id.
    """
    kwargs = self.request.resolver_match.kwargs
    value = dict((value, key)
                 for key, value in kwargs
                 .items())\
        .get(str(self.request.user.id))
    try:
        return bool(self.request.user.id == int(kwargs[value]))
    except KeyError:
        return False


def get_permissions(self):
    """
    Function to get the appropiate permission.
    """
    if try_match(self):
        return [IsObjectUser()]
    elif self.request.resolver_match.url_name == 'profile-me':
        return [IsAuthenticated()]
    return [DjangoModelPermissions()]


class ProfileViewSet(ModelViewSet):
    """
    Profile view set with appropiate permission handling.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        return get_permissions(self)

    # https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing
    @ action(detail=False, methods=['GET', 'PUT', 'DELETE'])
    # Add djoser's /me endpoint to /profile endpoint
    def me(self, request):
        if request.user.id:
            profile = Profile.objects.get(id=request.user.id)
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
    serializer_class = ProfileLinkSerializer

    def get_permissions(self):
        return get_permissions(self)

    def get_queryset(self):
        return Link.objects.filter(profile_id=self.kwargs['profile_pk'])

    def get_serializer_context(self):
        return {'profile_id': self.kwargs['profile_pk']}


class SocialViewSet(ModelViewSet):
    """
    Profile social view set with appropiate permission handling.
    """
    serializer_class = ProfileSocialSerializer

    def get_permissions(self):
        return get_permissions(self)

    def get_queryset(self):
        return Social.objects.filter(profile_id=self.kwargs['profile_pk'])

    def get_serializer_context(self):
        return {'profile_id': self.kwargs['profile_pk']}