from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated, AllowAny
from .models import Profile, Link, Social
from .serializers import ProfileSerializer, ProfileLinkSerializer, ProfileSocialSerializer


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [DjangoModelPermissions]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    # https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing
    @action(detail=False, methods=['GET', 'PUT'])
    def me(self, request):
        if request.user.id:
            (profile, created) = Profile.objects.get_or_create(id=request.user.id)
            if request.method == 'GET':
                serializer = ProfileSerializer(profile)
                return Response(serializer.data)
            elif request.method == 'PUT':
                serializer = ProfileSerializer(profile, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)
        else:
            return Response({
                "detail": "Authentication credentials were not provided."
            })


class LinkViewSet(ModelViewSet):
    serializer_class = ProfileLinkSerializer

    def get_queryset(self):
        return Link.objects.filter(profile_id=self.kwargs['profile_pk'])

    def get_serializer_context(self):
        return {'profile_id': self.kwargs['profile_pk']}


class SocialViewSet(ModelViewSet):
    serializer_class = ProfileSocialSerializer

    def get_queryset(self):
        return Social.objects.filter(profile_id=self.kwargs['profile_pk'])

    def get_serializer_context(self):
        return {'profile_id': self.kwargs['profile_pk']}
