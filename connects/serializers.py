from rest_framework import serializers
from core.models import User
from profiles.models import Profile
from .models import *


class ConnecterSerializer(serializers.ModelSerializer):
    """
    Connecter serializer to initiate the connection between
    two profiles.
    """
    class Meta:
        model = Connected
        fields = [
            'id', 'connecter_choice', 'connecting_choice'
        ]
        read_only_fields = [
            'connecting_choice',
        ]

    def create(self, validated_data):
        connecter_id = self.context['connecter_id']
        connecting_id = self.context['connecting_id']
        connecter_username = self.context['connecter_username']
        return Connected.objects.create(
            connecter_id=connecter_id,
            connecting_id=connecting_id,
            connecter_username=connecter_username,
            **validated_data)


class ConnectingSerializer(serializers.ModelSerializer):
    """
    Connecting serializer to handle the incomming connection
    between two profiles.
    """
    opposite_user = serializers.SerializerMethodField()

    class Meta:
        model = Connected
        fields = [
            'id', 'connecter_choice', 'connecting_choice',
            'connecter_username', 'opposite_user',
        ]
        read_only_fields = [
            'connecter_choice', 'connecter_username'
        ]

    def get_opposite_user(self, obj):
        opposite_user_id = 0
        if not obj.connecter_id == self.context['request_user_id']:
            opposite_user_id = obj.connecter_id
        else:
            opposite_user_id = obj.connecting_id

        profile = Profile.objects \
                         .select_related('user') \
                         .get(id=opposite_user_id)

        user_context = {}

        if profile.image:
            user_context['image'] = profile.image

        user_context['slug'] = profile.slug
        user_context['firstname'] = profile.user.first_name
        user_context['lastname'] = profile.user.last_name

        return user_context

    def update(self, instance, validated_data):
        instance.connecting_choice \
            = validated_data.get('connecting_choice')

        instance.save()

        return instance
