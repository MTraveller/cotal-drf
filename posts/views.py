from django.db.models import Prefetch
from rest_framework.viewsets import ModelViewSet
from core.do_permissions import do_permissions
from profiles.models import Profile
from tags.models import TaggedItem
from .models import *
from .serializers import *


class ProfilePostViewSet(ModelViewSet):
    """
    Profile post view set with appropiate permission handling.
    """
    queryset = Profile.objects \
        .prefetch_related('user__profile') \
        .prefetch_related('profileposts__postcomments__profile__user') \
        .all()

    serializer_class = ProfileSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        return do_permissions(self)


class PostViewSet(ModelViewSet):
    """
    Post view set with appropiate permission handling.
    """
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        return do_permissions(self)

    # https://docs.djangoproject.com/en/4.1/ref/models/querysets/#django.db.models.Prefetch
    def get_queryset(self):
        print(self.kwargs)
        return Post.objects \
            .prefetch_related('profile__user') \
            .prefetch_related('postcomments__profile__user') \
            .prefetch_related(Prefetch(
                'tags',
                queryset=TaggedItem.objects
                .select_related('tag')
                .all()
            )) \
            .filter(profile__slug=self.kwargs['profile_slug'])

    def get_serializer_context(self):
        user = Profile.objects.get(slug=self.kwargs['profile_slug'])

        return {'profile_id': user.id}  # type: ignore


class PostCommentViewSet(ModelViewSet):
    """
    Post comment view set with appropiate permission handling.
    """
    serializer_class = PostCommentSerializer

    def get_permissions(self):
        url_name = self.request.resolver_match.url_name

        if url_name == 'post-comments-detail':
            pk = self.request.resolver_match.kwargs['pk']
            comment_profile_id = PostComment.objects \
                .get(id=pk)
            self.__dict__['comment_profile_id'] \
                = comment_profile_id  # type: ignore

        return do_permissions(self)

    def get_queryset(self):
        url_name = self.request.resolver_match.url_name

        if not url_name == 'post-comments-detail':
            return PostComment.objects \
                .prefetch_related('profile__user') \
                .prefetch_related('post__profile__user') \
                .filter(post__slug=self.kwargs['post_slug'])
        pk = self.__dict__['kwargs']['pk']

        return PostComment.objects \
            .prefetch_related('profile__user') \
            .filter(id=pk)

    def get_serializer_context(self):
        post = Post.objects.get(slug=self.kwargs['post_slug'])

        return {
            'post_id': post.id,  # type: ignore
            'user_id': self.request.user.id,  # type: ignore
        }
