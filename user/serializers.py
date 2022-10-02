from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from .models import *


class UserCreateSerializer(BaseUserCreateSerializer):
    first_name = serializers.CharField(allow_blank=False)
    last_name = serializers.CharField(allow_blank=False)

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name']


class ProfileSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ['id', 'name', 'username']

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        return Social.objects.create(profile_id=profile_id, **validated_data)


class ProfileLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'title', 'link']

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        return Link.objects.create(profile_id=profile_id, **validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    # https://www.django-rest-framework.org/api-guide/relations/#nested-relationships
    links = ProfileLinkSerializer(many=True, read_only=True)
    socials = ProfileSocialSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id', 'user_id', 'image', 'status',
            'location', 'links', 'socials'
        ]
