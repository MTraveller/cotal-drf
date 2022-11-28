import json
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.template.defaultfilters import slugify
from rest_framework import serializers
from core.serializers import BaseProfileSerializer, ProfileUserSerializer
from tags.serializers import TaggedSerializer
from tags.models import Tag, TaggedItem
from .models import *


class PostCommentSerializer(serializers.ModelSerializer):
    """
    Post comment serializer to handle post comments
    1 level deep.
    """
    profile = BaseProfileSerializer(read_only=True)

    class Meta:
        model = PostComment
        fields = ['id', 'profile', 'created_on', 'comment']
        read_only_fields = ['profile', 'created_on']

    def create(self, validated_data):
        profile_id = self.context['user_id']
        post_id = self.context['post_id']
        return PostComment.objects \
            .create(
                profile_id=profile_id,
                post_id=post_id,
                **validated_data
            )


# https://www.django-rest-framework.org/api-guide/relations/#writable-nested-serializers
class PostSerializer(serializers.ModelSerializer):
    """
    Post serializer extends profile, postimages,
    postcomments and tagged serializers
    """

    profile = BaseProfileSerializer(read_only=True)
    comment_count = serializers.SerializerMethodField()
    postcomments = PostCommentSerializer(many=True, read_only=True)
    tags = TaggedSerializer(many=True, required=False)

    add_tags = serializers.ListField(
        child=serializers.CharField(
            max_length=50,
            allow_blank=True,
            trim_whitespace=True,
        ),
        required=False,
        write_only=True,
    )

    title = serializers.CharField(trim_whitespace=True)

    class Meta:
        model = Post
        fields = [
            'id', 'profile', 'image', 'title',
            'slug', 'created_on', 'post', 'tags', 'add_tags',
            'comment_count', 'postcomments'
        ]
        read_only_fields = ['slug', 'created_on', 'comment_count']

    def get_comment_count(self, obj):
        return obj.postcomments.count()

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        post_slug = slugify(validated_data['title'].strip())

        # filter with lambda to extract
        # targeted dicts from validated data
        data = dict(filter(
            lambda key: key[0] in [
                'tags', 'add_tags'
            ], validated_data.items()))

        if ('add_tags') in validated_data:
            # List comprehension to remove targeted dicts
            # from validated data.
            # # If working in backend without the frontend,
            # # add: tags to ['tags', 'add_tags']
            [validated_data.pop(key)
             for key in ['add_tags']]

        if Post.objects \
               .filter(profile_id=profile_id) \
               .filter(slug=post_slug).count() >= 1:
            raise serializers.ValidationError({
                'detail': 'You already have this %s title,'
                ' must be unique to your account.' % Post.__name__
            })
        else:
            if len(validated_data['title']) > 80:
                raise serializers.ValidationError({
                    'detail': 'The %s title,'
                    ' can max be 80 characters long.' % Post.__name__
                })
            else:
                post = Post.objects \
                           .create(
                               profile_id=profile_id, **validated_data)

        if 'add_tags' in data \
                and bool(len(data['add_tags'])):
            tags_data = ''
            if not str(data['add_tags']):
                tags_data = data.pop('add_tags')
            else:
                tags_data = data['add_tags'][0]
                data.pop('add_tags')

            content_type = ContentType.objects.get(model="post")

            print("tags_data", tags_data)
            # # If working in backend without the frontend,
            # # remove: [] from tags_data
            for label in [tags_data]:
                print(label)
                tag = ""
                label.lower()
                try:
                    tag = Tag.objects.get(label=label)
                except ObjectDoesNotExist:
                    tag = Tag.objects.create(label=label)

                TaggedItem.objects.create(
                    object_id=post.id,  # type: ignore
                    content_type=content_type,  # type: ignore
                    tag_id=tag.id  # type: ignore
                )

        return post

    def update(self, instance, validated_data):
        post_title = validated_data['title']

        tags = validated_data['tags'] if bool(
            'tags' in validated_data) else []

        # List comprehension to extract tags
        # within triple nested OrderedDicts.
        # O(n) = O(nx3)
        prev_tags = [
            list(list(tag)[0] for tag in (
                inner_dict_v.values()
                for key, inner_dict_v in outer_dict.items()
            ))[0] for outer_dict in tags
        ]

        queryset = Post.objects \
                       .filter(profile_id=instance.profile_id) \
                       .filter(title=post_title)

        if queryset.count() == 1 and not list(queryset)[0] == instance:
            raise serializers.ValidationError({
                'detail': 'You already have this %s title,'
                ' must be unique to your account.' % Post.__name__
            })
        else:
            if len(validated_data['title']) > 80:
                raise serializers.ValidationError({
                    'detail': 'The %s title,'
                    ' can max be 80 characters long.' % Post.__name__
                })
            else:
                instance.image = validated_data.get('image', instance.image)
                instance.title = validated_data.get('title', instance.title)
                instance.post = validated_data.get('post', instance.post)

                instance.save()

        # Queryset to grab all TaggedItems
        # for the edited post.
        queryset = TaggedItem.objects \
            .get_tags_for(
                Post,
                instance.id
            )

        # map with lambda to extract tag id & label
        # from the queryset above.
        # O(n)
        prev_tags_queryset = list(map(
            lambda tag: [
                tag._state.fields_cache['tag'].id,
                tag._state.fields_cache['tag'].label
            ], queryset
        ))

        prev_tags_queryset.sort()
        prev_tags.sort()

        # Code block checks previous tags against
        # validated tags and acts accordingly.
        # O(n) = (nx2)
        if len(prev_tags):
            for tag in prev_tags_queryset:
                if tag[1] in prev_tags:
                    continue
                else:
                    remove_tag = TaggedItem.objects \
                        .get(tag__label=tag[1])
                    TaggedItem.delete(remove_tag)
        else:
            # O(n)
            for tag in prev_tags_queryset:
                remove_tag = TaggedItem.objects \
                    .get(tag__label=tag[1])
                TaggedItem.delete(remove_tag)

        # Code block to check if new tags were added
        # and acts accordingly.
        if 'add_tags' in validated_data:
            # O(n)
            # # If working in backend without the frontend,
            # # remove: [0] on validated_data['add_tags']
            new_tags = list(map(
                lambda tag: tag.lower(), validated_data['add_tags'][0]
            ))

            content_type = ContentType.objects.get(model="post")

            # O(n)
            for label in new_tags:
                tag = ""
                try:
                    tag = Tag.objects.get(label=label)
                except ObjectDoesNotExist:
                    tag = Tag.objects.create(label=label)

                TaggedItem.objects.create(
                    object_id=instance.id,  # type: ignore
                    content_type=content_type,  # type: ignore
                    tag_id=tag.id  # type: ignore
                )

        return instance


class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile serializer extending profile user & post serializers.
    """
    # https://www.django-rest-framework.org/api-guide/relations/#nested-relationships
    user = ProfileUserSerializer(read_only=True)
    profileposts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'image', 'slug', 'profileposts']
