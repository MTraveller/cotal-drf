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
        .prefetch_related('profileposts__postimages') \
        .prefetch_related('profileposts__postcomments__profile__user') \
        .all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        return do_permissions(self)


class PostViewSet(ModelViewSet):
    """
    Post view set with appropiate permission handling.
    """
    serializer_class = PostSerializer

    def get_permissions(self):
        return do_permissions(self)

    # https://docs.djangoproject.com/en/4.1/ref/models/querysets/#django.db.models.Prefetch
    def get_queryset(self):
        return Post.objects \
            .prefetch_related('profile__user') \
            .prefetch_related('postimages__profileposts') \
            .prefetch_related('postcomments__profile__user') \
            .prefetch_related(Prefetch(
                'tags',
                queryset=TaggedItem.objects
                .select_related('tag')
                .all()
            )) \
            .filter(profile_id=self.kwargs['profile_pk'])

    def get_serializer_context(self):
        return {'profile_id': self.kwargs['profile_pk']}


# class PostImageViewSet(ModelViewSet):
#     """
#     Post image view set with appropiate permission handling.
#     """
#     serializer_class = PostImageSerializer

#     def get_permissions(self):
#         return do_permissions(self)

#     def get_queryset(self):
#         return PostImage.objects \
#             .select_related('post__profile__user') \
#             .filter(profile_id=self.kwargs['profiles_pk'])

#     def get_serializer_context(self):
#         return {'profile_id': self.kwargs['profiles_pk']}


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
            self.__dict__['comment_profile_id'] = comment_profile_id
        return do_permissions(self)

    def get_queryset(self):
        url_name = self.request.resolver_match.url_name
        if not url_name == 'post-comments-detail':
            return PostComment.objects \
                .prefetch_related('profile__user') \
                .prefetch_related('post__profile__user') \
                .filter(post_id=self.kwargs['post_pk'])
        pk = self.__dict__['kwargs']['pk']
        return PostComment.objects \
            .prefetch_related('profile__user') \
            .filter(id=pk)

    def get_serializer_context(self):
        return {
            'post_id': self.kwargs['post_pk'],
            'user_id': self.request.user.id,  # type: ignore
        }
