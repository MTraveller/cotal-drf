from rest_framework import serializers
from core.serializers import ProfileUserSerializer
from .models import *


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment']
        read_only_fields = ['id']


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image']
        read_only_fields = ['id']


class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)
    comments = PostCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'post', 'images', 'comments']
        read_only_fields = ['slug']

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        return Post.objects.create(profile_id=profile_id, **validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    # https://www.django-rest-framework.org/api-guide/relations/#nested-relationships
    user = ProfileUserSerializer(read_only=True)
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'user', 'posts',
        ]
