from rest_framework import serializers
from .models import *


class ConnecterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connected
        fields = [
            'id', 'connecter_choice', 'connecting_choice',
            'connecter_id', 'connecting_id',
        ]

    def create(self, validated_data):
        connecter_id = self.context['connecter_id']
        connecting_id = self.context['connecting_id']
        return Connected.objects.create(
            connecter_id=connecter_id,
            connecting_id=connecting_id,
            **validated_data)


class ConnectingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connected
        fields = [
            'id', 'connecter_choice', 'connecting_choice',
            'connecter_id', 'connecting_id',
        ]

    def update(self, instance, validated_data):
        instance.connecting_choice = validated_data.get('connecting_choice')
        instance.save()
        return instance
