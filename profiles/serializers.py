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
        title = validated_data['title']

        queryset = Portfolio.objects.filter(
            profile_id=profile_id).filter(title=title)
        if queryset.count() == 1:
            raise serializers.ValidationError({
                'detail': 'You already have this %s title,'
                ' must be unique to your account.' % Portfolio.__name__
            })
        else:
            if len(validated_data['title']) > 80:
                raise serializers.ValidationError({
                    'detail': 'The %s title,'
                    ' can max be 80 characters long.' % Portfolio.__name__
                })
            else:

                return Portfolio.objects \
                    .create(profile_id=profile_id, **validated_data)

    def update(self, instance, validated_data):
        profile_id = self.context['profile_id']
        title = validated_data['title']

        queryset = Portfolio.objects.filter(
            profile_id=profile_id).filter(title=title)
        if queryset.count() == 1 and not list(queryset)[0] == instance:
            raise serializers.ValidationError({
                'detail': 'You already have this %s title,'
                ' must be unique to your account.' % Portfolio.__name__
            })
        else:
            if len(validated_data['title']) > 80:
                raise serializers.ValidationError({
                    'detail': 'The %s title,'
                    ' can max be 80 characters long.' % Portfolio.__name__
                })
            else:
                if not 'image' in validated_data and \
                        self.initial_data['remove_image'] == 'true':  # type: ignore
                    instance.image = None
                return super().update(instance, validated_data)


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
        title = validated_data['title']

        queryset = Award.objects.filter(
            profile_id=profile_id).filter(title=title)
        if queryset.count() == 1:
            raise serializers.ValidationError({
                'detail': 'You already have this %s title,'
                ' must be unique to your account.' % Award.__name__
            })
        else:
            if len(validated_data['title']) > 80:
                raise serializers.ValidationError({
                    'detail': 'The %s title,'
                    ' can max be 80 characters long.' % Award.__name__
                })
            else:
                return Award.objects \
                    .create(profile_id=profile_id, **validated_data)

    def update(self, instance, validated_data):
        profile_id = self.context['profile_id']
        title = validated_data['title']

        queryset = Award.objects.filter(
            profile_id=profile_id).filter(title=title)
        if queryset.count() == 1 and not list(queryset)[0] == instance:
            raise serializers.ValidationError({
                'detail': 'You already have this %s title,'
                ' must be unique to your account.' % Award.__name__
            })
        else:
            if len(validated_data['title']) > 80:
                raise serializers.ValidationError({
                    'detail': 'The %s title,'
                    ' can max be 80 characters long.' % Award.__name__
                })
            else:
                if not 'image' in validated_data and \
                        self.initial_data['remove_image'] == 'true':  # type: ignore
                    instance.image = None
                return super().update(instance, validated_data)


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
        title = validated_data['title']

        queryset = Certificate.objects.filter(
            profile_id=profile_id).filter(title=title)
        if queryset.count() == 1:
            raise serializers.ValidationError({
                'detail': 'You already have this %s title,'
                ' must be unique to your account.' % Certificate.__name__
            })
        else:
            if len(validated_data['title']) > 80:
                raise serializers.ValidationError({
                    'detail': 'The %s title,'
                    ' can max be 80 characters long.' % Certificate.__name__
                })
            else:
                return Certificate.objects \
                    .create(profile_id=profile_id, **validated_data)

    def update(self, instance, validated_data):
        profile_id = self.context['profile_id']
        title = validated_data['title']

        queryset = Certificate.objects.filter(
            profile_id=profile_id).filter(title=title)
        if queryset.count() == 1 and not list(queryset)[0] == instance:
            raise serializers.ValidationError({
                'detail': 'You already have this %s title,'
                ' must be unique to your account.' % Certificate.__name__
            })
        else:
            if len(validated_data['title']) > 80:
                raise serializers.ValidationError({
                    'detail': 'The %s title,'
                    ' can max be 80 characters long.' % Certificate.__name__
                })
            else:
                if not 'image' in validated_data and \
                        self.initial_data['remove_image'] == 'true':  # type: ignore
                    instance.image = None
                return super().update(instance, validated_data)


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
        title = validated_data['title']

        queryset = Creative.objects.filter(
            profile_id=profile_id).filter(title=title)
        if queryset.count() == 1:
            raise serializers.ValidationError({
                'detail': 'You already have this %s title,'
                ' must be unique to your account.' % Creative.__name__
            })
        else:
            if len(validated_data['title']) > 80:
                raise serializers.ValidationError({
                    'detail': 'The %s title,'
                    ' can max be 80 characters long.' % Creative.__name__
                })
            else:
                return Creative.objects \
                    .create(profile_id=profile_id, **validated_data)

    def update(self, instance, validated_data):
        profile_id = self.context['profile_id']
        title = validated_data['title']

        queryset = Creative.objects.filter(
            profile_id=profile_id).filter(title=title)
        if queryset.count() == 1 and not list(queryset)[0] == instance:
            raise serializers.ValidationError({
                'detail': 'You already have this %s title,'
                ' must be unique to your account.' % Creative.__name__
            })
        else:
            if len(validated_data['title']) > 80:
                raise serializers.ValidationError({
                    'detail': 'The %s title,'
                    ' can max be 80 characters long.' % Creative.__name__
                })
            else:
                if not 'image' in validated_data and \
                        self.initial_data['remove_image'] == 'true':  # type: ignore
                    instance.image = None
                return super().update(instance, validated_data)


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
    Profile serializer that extends user, linktrees and socials.
    """
    # https://www.django-rest-framework.org/api-guide/relations/#nested-relationships
    user = ProfileUserSerializer(read_only=True)
    linktrees = ProfileLinktreeSerializer(many=True, read_only=True)
    socials = ProfileSocialSerializer(many=True, read_only=True)

    image = serializers.ImageField(required=False)
    slug = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'slug',
            'image', 'status', 'location',
            'linktrees', 'socials',
        ]

    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.status = validated_data.get('status', instance.status)
        instance.location = validated_data.get('location', instance.location)

        if not 'image' in validated_data and \
                self.initial_data['remove_image'] == 'true':  # type: ignore
            instance.image = None

        instance.save()

        return instance
