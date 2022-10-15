from rest_framework import serializers
from djoser.serializers import (
    UserSerializer as BaseUserSerializer,
    UserCreateSerializer as BaseUserCreateSerializer
)

from profiles.models import Profile


class UserCreateSerializer(BaseUserCreateSerializer):
    first_name = serializers.CharField(allow_blank=False)
    last_name = serializers.CharField(allow_blank=False)

    class Meta(BaseUserCreateSerializer.Meta):
        fields = [
            'id', 'username', 'password',
            'email', 'first_name', 'last_name'
        ]


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = [
            'id', 'username', 'email',
            'first_name', 'last_name'
        ]


class ProfileUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['first_name', 'last_name']


class BaseProfileSerializer(serializers.ModelSerializer):
    user = ProfileUserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'slug', 'image']
