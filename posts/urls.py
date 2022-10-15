from rest_framework_nested import routers
from . import views


# Guide source:
# https://github.com/alanjds/drf-nested-routers#quickstart
router = routers.DefaultRouter()
router.register(
    'profiles', views.ProfilePostViewSet, basename='profiles')

# https://github.com/alanjds/drf-nested-routers#infinite-depth-nesting
post_router = routers.NestedDefaultRouter(
    router, 'profiles', lookup='profile'
)
post_router.register('posts', views.PostViewSet, basename='posts')
# post_router.register('post-images', views.PostImageViewSet,
#                      basename='profile-postimages')

post_comments_router = routers.NestedDefaultRouter(
    post_router, 'posts', lookup='post')
post_comments_router.register(
    'comments', views.PostCommentViewSet, basename='post-comments')


urlpatterns = router.urls + post_router.urls + post_comments_router.urls
