from rest_framework import serializers
from .models import Tag, TaggedItem


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'label', 'slug'
        ]
        read_only_fields = ['slug']


class TaggedSerializer(serializers.ModelSerializer):
    tag = TagSerializer()

    class Meta:
        model = TaggedItem
        fields = [
            'tag'
        ]
