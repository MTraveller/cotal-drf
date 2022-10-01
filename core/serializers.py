from rest_framework import serializers
from .models import *


class ProfileLinkSerializer(serializers.Serializer):
    class Meta:
        model = ProfileLink
        fields = ['id', 'external', 'social']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'image', 'status', 'link']
        