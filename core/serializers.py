from rest_framework import serializers
from djoser.serializers import (
    UserSerializer as BaseUserSerializer,
    UserCreateSerializer as BaseUserCreateSerializer
)
from profiles.serializers import *
from .models import *


class UserCreateSerializer(BaseUserCreateSerializer):
    first_name = serializers.CharField(allow_blank=False)
    last_name = serializers.CharField(allow_blank=False)

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class ProfileUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['first_name', 'last_name']


class ProfileSerializer(serializers.ModelSerializer):
    # https://www.django-rest-framework.org/api-guide/relations/#nested-relationships
    user = ProfileUserSerializer(read_only=True)
    linktrees = ProfileLinktreeSerializer(many=True, read_only=True)
    socials = ProfileSocialSerializer(many=True, read_only=True)
    portfolios = ProfilePortfolioSerializer(many=True, read_only=True)
    awards = ProfileAwardSerializer(many=True, read_only=True)
    certificates = ProfileCertificateSerializer(many=True, read_only=True)
    creatives = ProfileCreativeSerializer(many=True, read_only=True)
    settings = ProfileSettingSerializer(many=True, read_only=True)

    slug = serializers.CharField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            'user', 'slug', 'image', 'status',
            'location', 'linktrees', 'socials',
            'portfolios', 'awards', 'certificates',
            'creatives', 'settings'
        ]
