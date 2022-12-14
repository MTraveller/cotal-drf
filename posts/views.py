from django.http import Http404
from django.db.models import Prefetch
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from core.do_permissions import do_permissions, IsNotObjectUserOrReadOnly
from profiles.models import Profile
from tags.models import TaggedItem
from .models import *
from .serializers import *
from .pagination import DefaultPagination


class PostsViewSet(ModelViewSet):
    ordering_fields = ['created_on']
    pagination_class = DefaultPagination
    serializer_class = PostSerializer

    def get_permissions(self):
        return [IsNotObjectUserOrReadOnly()]

    def get_queryset(self):
        queryset = Post.objects \
            .prefetch_related('profile__user') \
            .prefetch_related('postcomments__profile__user') \
            .all()

        if self.request.user.is_authenticated:
            queryset = queryset.exclude(
                profile_id=self.request.user.id)  # type: ignore

        return queryset


class ProfilePostViewSet(ModelViewSet):
    """
    Profile post view set with appropiate permission handling.
    """
    parser_classes = (
        MultiPartParser,
        FormParser,
    )
    lookup_field = 'slug'
    ordering_fields = ['profileposts__created_on']
    pagination_class = DefaultPagination
    serializer_class = ProfileSerializer

    def get_permissions(self):
        return do_permissions(self)

    def get_queryset(self):
        queryset = Profile.objects \
            .prefetch_related('user__profile') \
            .prefetch_related('profileposts__postcomments__profile__user') \
            .all()

        if self.request.user.is_authenticated:
            queryset = queryset.exclude(
                id=self.request.user.id)  # type: ignore

        return queryset


class PostViewSet(ModelViewSet):
    """
    Post view set with appropiate permission handling.
    """
    parser_classes = (
        MultiPartParser,
        FormParser,
    )
    lookup_field = 'slug'
    serializer_class = PostSerializer

    def get_permissions(self):
        return do_permissions(self)

    # https://docs.djangoproject.com/en/4.1/ref/models/querysets/#django.db.models.Prefetch
    def get_queryset(self):
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
        try:
            user = Profile.objects.get(slug=self.kwargs['profile_slug'])

            return {'profile_id': user.id}  # type: ignore
        except:
            raise Http404


class PostCommentViewSet(ModelViewSet):
    """
    Post comment view set with appropiate permission handling.
    """
    serializer_class = PostCommentSerializer

    def get_permissions(self):
        url_name = self.request.resolver_match.url_name

        if url_name == 'post-comments-detail':
            pk = self.request.resolver_match.kwargs['pk']

            try:
                comment_profile_id = PostComment.objects \
                    .get(id=pk)
                self.__dict__['comment_profile_id'] \
                    = comment_profile_id  # type: ignore
            except:
                pass

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
        try:
            post = Post.objects.get(slug=self.kwargs['post_slug'])

            return {
                'post_id': post.id,  # type: ignore
                'user_id': self.request.user.id,  # type: ignore
            }

        except:
            raise Http404
