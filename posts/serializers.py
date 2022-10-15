from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from core.serializers import BaseProfileSerializer, ProfileUserSerializer
from tags.serializers import TaggedSerializer
from tags.models import Tag, TaggedItem
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
        fields = ['id', 'profile', 'title', 'slug',
                  'post', 'tags', 'add_tags', 'postimages', 'postcomments']
        read_only_fields = ['slug']

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        data = validated_data.copy()
        print(data)
        if ('add_tags' or 'postimages') in validated_data:
            [validated_data.pop(key)
             for key in ['tags', 'add_tags', 'postimages']]
        post = Post.objects \
            .create(profile_id=profile_id, **validated_data)

        if 'add_tags' in data \
                and bool(len(data['add_tags'])):
            tags_data = data.pop('add_tags')
            print(tags_data)
            tags_data = [tag.lower() for tag in tags_data]
            content_type_id = ContentType.objects.get(model="post").id

            for label in tags_data:
                tag = ""
                try:
                    tag = Tag.objects.get(label=label)
                except ObjectDoesNotExist:
                    tag = Tag.objects.create(label=label)

                TaggedItem.objects.create(
                    object_id=post.id,  # type: ignore
                    content_type_id=content_type_id,  # type: ignore
                    tag_id=tag.id  # type: ignore
                )

        if 'postimages' in data \
                and bool(len(data['postimages'])):
            images_data = data.pop('postimages')
            for image_data in images_data:
                PostImage.objects.create(
                    profile_id=profile_id, post=post, **image_data)

        return post

    def update(self, instance, validated_data):
        updated_tags = validated_data['tags']

        validated_tags = []
        for dict in updated_tags:
            for inner_dict in dict.values():
                for tag in inner_dict.values():
                    validated_tags.append(tag)

        queryset = TaggedItem.objects \
            .get_tags_for(
                Post,
                instance.id
            )

        previous_tags = list(map(
            lambda tag: [
                tag._state.fields_cache['tag'].id,
                tag._state.fields_cache['tag'].label
            ], queryset
        ))

        previous_tags.sort()
        validated_tags.sort()

        if len(validated_tags):
            for tag in previous_tags:
                if tag[1] in validated_tags:
                    continue
                else:
                    remove_tag = TaggedItem.objects \
                        .get(tag__label=tag[1])
                    TaggedItem.delete(remove_tag)
        else:
            for tag in previous_tags:
                remove_tag = TaggedItem.objects \
                    .get(tag__label=tag[1])
                TaggedItem.delete(remove_tag)

        if 'add_tags' in validated_data:
            new_tags = list(map(
                lambda tag: tag.lower(), validated_data['add_tags']
            ))

            content_type_id = ContentType.objects.get(model="post").id

            for label in new_tags:
                tag = ""
                try:
                    tag = Tag.objects.get(label=label)
                except ObjectDoesNotExist:
                    tag = Tag.objects.create(label=label)

                TaggedItem.objects.create(
                    object_id=instance.id,  # type: ignore
                    content_type_id=content_type_id,  # type: ignore
                    tag_id=tag.id  # type: ignore
                )

        return instance


class ProfileSerializer(serializers.ModelSerializer):
    # https://www.django-rest-framework.org/api-guide/relations/#nested-relationships
    user = ProfileUserSerializer(read_only=True)
    profileposts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'image', 'slug', 'profileposts']
