from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from .models import *


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']


class ProfileSocialLink(serializers.ModelSerializer):
    class Meta:
        model = SocialUsername
        fields = ['id', 'social_media', 'social_username']


class ProfileLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileLink
        fields = ['id', 'external', 'social_id', 'social_links']

    social_links = ProfileSocialLink()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user_id', 'image', 'status', 'location', 'link_id', 'profile_links']

    profile_links = ProfileLinkSerializer()
