from rest_framework import serializers
from connects.serializers import ConnecterSerializer, ConnectingSerializer
from follows.serializers import FollowSerializer, FollowingSerializer
from core.serializers import ProfileUserSerializer
from .models import *


class ProfileLinktreeSerializer(serializers.ModelSerializer):
    """
    Profile linktree serializer.
    """

    class Meta:
        model = Linktree
        fields = ['username']

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
    class Meta:
        model = Portfolio
        fields = ['id', 'image', 'title', 'description', 'link']

    def create(self, validated_data):
        profile_id = self.context['profile_id']

        return Portfolio.objects \
                        .create(profile_id=profile_id, **validated_data)


class ProfileAwardSerializer(serializers.ModelSerializer):
    """
    Profile award serializer.
    """
    class Meta:
        model = Award
        fields = ['id', 'image', 'title', 'description', 'link']

    def create(self, validated_data):
        profile_id = self.context['profile_id']

        return Award.objects \
                    .create(profile_id=profile_id, **validated_data)


class ProfileCertificateSerializer(serializers.ModelSerializer):
    """
    Profile certificate serializer.
    """
    class Meta:
        model = Certificate
        fields = ['id', 'image', 'title', 'description', 'link']

    def create(self, validated_data):
        profile_id = self.context['profile_id']

        return Certificate.objects \
                          .create(profile_id=profile_id, **validated_data)


class ProfileCreativeSerializer(serializers.ModelSerializer):
    """
    Profile creative serializer.
    """
    class Meta:
        model = Creative
        fields = ['id', 'title', 'description', 'link']

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
    # portfolios = ProfilePortfolioSerializer(many=True, read_only=True)
    # awards = ProfileAwardSerializer(many=True, read_only=True)
    # certificates = ProfileCertificateSerializer(many=True, read_only=True)
    # creatives = ProfileCreativeSerializer(many=True, read_only=True)
    # settings = ProfileSettingSerializer(many=True, read_only=True)
    # connecters = ConnecterSerializer(many=True, read_only=True)
    # connectings = ConnectingSerializer(many=True, read_only=True)
    # followers = FollowSerializer(many=True, read_only=True)
    # followings = FollowingSerializer(many=True, read_only=True)

    slug = serializers.CharField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'slug', 'image', 'status', 'location', 'linktrees', 'socials',
            # 'portfolios',
            # 'awards', 'certificates', 'creatives', 'settings',
            # 'connecters', 'connectings', 'followers', 'followings',
        ]
        lookup_field = ['slug']
