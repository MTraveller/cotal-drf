from rest_framework import serializers
from .models import Tag, TaggedItem


class TagSerializer(serializers.ModelSerializer):
    """
    Tag serializer.
    """
    class Meta:
        model = Tag
        fields = [
            'label', 'slug'
        ]
        read_only_fields = ['slug']


class TaggedSerializer(serializers.ModelSerializer):
    """
    Tagged serializer extends tag serializer.
    """
    tag = TagSerializer()

    class Meta:
        model = TaggedItem
        fields = [
            'tag'
        ]
