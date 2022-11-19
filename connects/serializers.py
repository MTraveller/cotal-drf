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
    connecter_image = serializers.SerializerMethodField()
    connecter_name = serializers.SerializerMethodField()

    class Meta:
        model = Connected
        fields = [
            'id', 'connecter_choice', 'connecting_choice',
            'connecter_image', 'connecter_name', 'connecter_username'
        ]
        read_only_fields = [
            'connecter_choice', 'connecter_username'
        ]

    def get_connecter_image(self, obj):
        connecter_id = obj.connecter_id
        user = Profile.objects.get(id=connecter_id)

        if user.image:
            return {'image': user.image}

    def get_connecter_name(self, obj):
        connecter_id = obj.connecter_id
        user = User.objects.get(id=connecter_id)

        return {'firstname': user.first_name, 'lastname': user.last_name}

    def update(self, instance, validated_data):
        instance.connecting_choice \
            = validated_data.get('connecting_choice')

        instance.save()

        return instance
