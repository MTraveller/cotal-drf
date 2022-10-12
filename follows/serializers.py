from rest_framework import serializers
from .models import *


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Followed
        fields = [
            'id', 'follower_choice',
            'following', 'followed',
        ]
        read_only_fields = [
            'following', 'followed'
        ]

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        followed_id = self.context['followed_id']
        return Followed.objects.create(
            profile_id=profile_id,
            followed_id=followed_id,
            **validated_data)
