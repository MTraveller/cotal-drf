from rest_framework import serializers
from .models import *


class ConnecterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connected
        fields = ['connecter_choice']

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
        fields = ['connecting_choice']

    def save(self, validated_data):
        id = self.context['id']
        connecting_id = self.context['connecting_id']
        object = Connected.objects.get(id=id)
