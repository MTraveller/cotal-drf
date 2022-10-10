from rest_framework import serializers
from core.serializers import BaseProfileSerializer, ProfileUserSerializer
from .models import *


class PostCommentSerializer(serializers.ModelSerializer):
    profile = BaseProfileSerializer(read_only=True)

    class Meta:
        model = PostComment
        fields = ['id', 'profile', 'comment']
        read_only_fields = ['profile']

    def create(self, validated_data):
        profile_id = self.context['user_id']
        post_id = self.context['post_id']
        return PostComment.objects.create(profile_id=profile_id, post_id=post_id, **validated_data)


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id', 'image']

    # TODO: Test post images creation on frontend!
    # def create(self, validated_data):
    #     profile_id = self.context['profile_id']
    #     return PostImage.objects.create(profile_id=profile_id, **validated_data)


# https://www.django-rest-framework.org/api-guide/relations/#writable-nested-serializers
class PostSerializer(serializers.ModelSerializer):
    profile = BaseProfileSerializer(read_only=True)
    postimages = PostImageSerializer(many=True, required=False)
    postcomments = PostCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'profile', 'title', 'slug',
                  'post', 'postimages', 'postcomments']
        read_only_fields = ['slug']

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        post = Post.objects.create(profile_id=profile_id, **validated_data)
        if 'postimages' in validated_data:
            images_data = validated_data.pop('postimages')
            for image_data in images_data:
                PostImage.objects.create(
                    profile_id=profile_id, post=post, **image_data)
        return post


class ProfileSerializer(serializers.ModelSerializer):
    # https://www.django-rest-framework.org/api-guide/relations/#nested-relationships
    user = ProfileUserSerializer(read_only=True)
    profileposts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'image', 'slug', 'profileposts']
