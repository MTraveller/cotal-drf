from rest_framework import serializers


class ProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    image = serializers.ImageField()
    status = serializers.CharField(max_length=255)
