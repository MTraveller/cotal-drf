from rest_framework import serializers
from djoser.serializers import (
    UserSerializer as BaseUserSerializer,
    UserCreateSerializer as BaseUserCreateSerializer
)
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


class ProfilePortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'image', 'title', 'description', 'link']

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        return Portfolio.objects.create(profile_id=profile_id, **validated_data)


class ProfileAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ['id', 'image', 'title', 'description', 'link']

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        return Award.objects.create(profile_id=profile_id, **validated_data)


class ProfileCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'image', 'title', 'description', 'link']

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        return Certificate.objects.create(profile_id=profile_id, **validated_data)


class ProfileCreativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creative
        fields = ['id', 'title', 'description', 'link']

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        return Creative.objects.create(profile_id=profile_id, **validated_data)


class ProfileSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = []

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        return Setting.objects.create(profile_id=profile_id, **validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    # https://www.django-rest-framework.org/api-guide/relations/#nested-relationships
    links = ProfileLinkSerializer(many=True, read_only=True)
    socials = ProfileSocialSerializer(many=True, read_only=True)
    portfolio = ProfilePortfolioSerializer(many=True, read_only=True)
    award = ProfileAwardSerializer(many=True, read_only=True)
    certificate = ProfileCertificateSerializer(many=True, read_only=True)
    creative = ProfileCreativeSerializer(many=True, read_only=True)
    setting = ProfileSettingSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = [
            'user_id', 'image', 'status',
            'location', 'links', 'socials',
            'portfolio', 'award', 'certificate',
            'creative', 'setting'
        ]
