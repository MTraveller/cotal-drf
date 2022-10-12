from rest_framework import serializers
from .models import *


class ConnecterSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = Connected
        fields = [
            'id', 'connecter_choice', 'connecting_choice',
            'connecter_choice', 'connecter_username',
        ]
        read_only_fields = [
            'connecter_username'
        ]

    def update(self, instance, validated_data):
        instance.connecting_choice = validated_data.get('connecting_choice')
        instance.save()
        return instance
