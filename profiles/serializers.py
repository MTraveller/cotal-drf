from rest_framework import serializers
from .models import *


class ProfileLinktreeSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField()

    class Meta:
        model = Linktree
        fields = ['id', 'title', 'username']

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        return Linktree.objects\
            .create(profile_id=profile_id, **validated_data)

    def save(self, *args, **kwargs):
        profile_id = self.context['profile_id']
        if Linktree.objects.filter(profile_id=profile_id).count() >= 1:
            raise serializers.ValidationError({
                'detail': 'You can only have 1 %s link' % Linktree.__name__
            })
        else:
            super().save(*args, **kwargs)


class ProfileSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ['id', 'name', 'username']

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        return Social.objects.create(profile_id=profile_id, **validated_data)


class ProfilePortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'image', 'title', 'description', 'link']

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        return Portfolio.objects\
                        .create(profile_id=profile_id, **validated_data)


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
        return Certificate.objects\
                          .create(profile_id=profile_id, **validated_data)


class ProfileCreativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creative
        fields = ['id', 'title', 'description', 'link']

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        return Creative.objects\
                       .create(profile_id=profile_id, **validated_data)


class ProfileSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = ['activity']

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        return Setting.objects.create(profile_id=profile_id, **validated_data)