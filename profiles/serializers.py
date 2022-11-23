from rest_framework import serializers
from connects.serializers import ConnecterSerializer, ConnectingSerializer
from follows.serializers import FollowSerializer, FollowingSerializer
from core.serializers import BaseProfileSerializer, ProfileUserSerializer
from .models import *


class ProfileLinktreeSerializer(serializers.ModelSerializer):
    """
    Profile linktree serializer.
    """

    class Meta:
        model = Linktree
        fields = ['id', 'username']

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        if Linktree.objects.filter(profile_id=profile_id).count() >= 1:
            raise serializers.ValidationError({
                'detail': 'You can only have 1 %s link' % Linktree.__name__
            })
        else:
            return Linktree.objects \
                           .create(profile_id=profile_id, **validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class ProfileSocialSerializer(serializers.ModelSerializer):
    """
    Profile social serializer.
    """
    class Meta:
        model = Social
        fields = ['id', 'name', 'username']

    def create(self, validated_data):
        profile_id = self.context['profile_id']

        if Social.objects \
                 .filter(profile_id=profile_id) \
                 .filter(name=validated_data['name']).count() >= 1:
            raise serializers.ValidationError({
                'detail':
                'You can only have 1 %s link' % validated_data['name']
            })
        else:
            return Social.objects \
                         .create(profile_id=profile_id, **validated_data)


class ProfilePortfolioSerializer(serializers.ModelSerializer):
    """
    Profile portfolio serializer.
    """
    profile = BaseProfileSerializer(read_only=True)

    class Meta:
        model = Portfolio
        fields = [
            'id', 'profile', 'image', 'title',
            'slug', 'description', 'link',
            'created_on',
        ]
        read_only_fields = ['slug', 'created_on', ]

    def create(self, validated_data):
        profile_id = self.context['profile_id']

        return Portfolio.objects \
                        .create(profile_id=profile_id, **validated_data)


class ProfileAwardSerializer(serializers.ModelSerializer):
    """
    Profile award serializer.
    """
    profile = BaseProfileSerializer(read_only=True)

    class Meta:
        model = Award
        fields = [
            'id', 'profile', 'image', 'title',
            'slug', 'description', 'link',
            'created_on',
        ]
        read_only_fields = ['slug', 'created_on', ]

    def create(self, validated_data):
        profile_id = self.context['profile_id']

        return Award.objects \
                    .create(profile_id=profile_id, **validated_data)


class ProfileCertificateSerializer(serializers.ModelSerializer):
    """
    Profile certificate serializer.
    """
    profile = BaseProfileSerializer(read_only=True)

    class Meta:
        model = Certificate
        fields = [
            'id', 'profile', 'image', 'title',
            'slug', 'description', 'link',
            'created_on',
        ]
        read_only_fields = ['slug', 'created_on', ]

    def create(self, validated_data):
        profile_id = self.context['profile_id']

        return Certificate.objects \
                          .create(profile_id=profile_id, **validated_data)


class ProfileCreativeSerializer(serializers.ModelSerializer):
    """
    Profile creative serializer.
    """
    profile = BaseProfileSerializer(read_only=True)

    class Meta:
        model = Creative
        fields = [
            'id', 'profile', 'image', 'title',
            'slug', 'description', 'link',
            'created_on',
        ]
        read_only_fields = ['slug', 'created_on', ]

    def create(self, validated_data):
        profile_id = self.context['profile_id']

        return Creative.objects \
                       .create(profile_id=profile_id, **validated_data)


class ProfileSettingSerializer(serializers.ModelSerializer):
    """
    Profile setting serializer.
    """
    class Meta:
        model = Setting
        fields = ['activity']

    def create(self, validated_data):
        raise serializers.ValidationError({
            'detail': 'You can only have 1 %s instance' % Setting.__name__
        })


class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile serializer that extends all above,
    connecter, connecting, follow and following serializers.
    """
    # https://www.django-rest-framework.org/api-guide/relations/#nested-relationships
    user = ProfileUserSerializer(read_only=True)
    linktrees = ProfileLinktreeSerializer(many=True, read_only=True)
    socials = ProfileSocialSerializer(many=True, read_only=True)

    slug = serializers.CharField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'slug',
            'image', 'status', 'location',
            'linktrees', 'socials',
        ]
        # lookup_field = ['slug']
