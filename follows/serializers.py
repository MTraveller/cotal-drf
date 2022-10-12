from rest_framework import serializers
from .models import *


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Followed
        fields = [
            'id', 'follower_choice', 'followed_by_slug',
        ]
        read_only_fields = [
            'followed_by_slug'
        ]

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        followed_by_id = self.context['followed_by_id']
        followed_by_slug = self.context['followed_by_slug']

        return Followed.objects.create(
            profile_id=profile_id,
            followed_by_id=followed_by_id,
            followed_by_slug=followed_by_slug,
            **validated_data)
