from rest_framework import serializers
from djoser.serializers import (
    UserSerializer as BaseUserSerializer,
    UserCreateSerializer as BaseUserCreateSerializer
)

from profiles.models import Profile


class UserCreateSerializer(BaseUserCreateSerializer):
    """
    User create serializer to be used on signup.
    """
    first_name = serializers.CharField(allow_blank=False)
    last_name = serializers.CharField(allow_blank=False)

    class Meta(BaseUserCreateSerializer.Meta):
        fields = [
            'id', 'username', 'password',
            'email', 'first_name', 'last_name'
        ]


class UserSerializer(BaseUserSerializer):
    """
    User serializer to send user details.
    """
    class Meta(BaseUserSerializer.Meta):
        fields = [
            'id', 'username', 'email',
            'first_name', 'last_name'
        ]


class ProfileUserSerializer(BaseUserSerializer):
    """
    User first name, last name serializer.
    """
    class Meta(BaseUserSerializer.Meta):
        fields = ['first_name', 'last_name']


class BaseProfileSerializer(serializers.ModelSerializer):
    """
    User slug and image serializer extends ProfileUserSerializer.
    """
    user = ProfileUserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'slug', 'image']
