from rest_framework import serializers
from .models import *


class FollowSerializer(serializers.ModelSerializer):
    """
    Follow serializer to handle follow requests.
    """
    class Meta:
        model = Followed
        fields = [
            'follower_choice', 'followed_by_name',
            'followed_by_username',
        ]
        read_only_fields = [
            'followed_by_username', 'followed_by_name',
        ]

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        followed_by_id = self.context['followed_by_id']
        followed_by_name = self.context['followed_by_name']
        followed_by_username = self.context['followed_by_username']
        following_by_name = self.context['following_by_name']
        following_by_username = self.context['following_by_username']

        return Followed.objects.create(
            profile_id=profile_id,
            followed_by_id=followed_by_id,
            followed_by_name=followed_by_name,
            followed_by_username=followed_by_username,
            following_by_name=following_by_name,
            following_by_username=following_by_username,
            **validated_data
        )


class FollowingSerializer(serializers.ModelSerializer):
    """
    Following serializer to show current followings.
    """
    class Meta:
        model = Followed
        fields = [
            'id', 'following_by_name', 'following_by_username',
        ]
        read_only_fields = [
            'following_by_name', 'following_by_username',
        ]
