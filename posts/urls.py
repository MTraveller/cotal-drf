from rest_framework_nested import routers
from . import views


# Guide source:
# https://github.com/alanjds/drf-nested-routers#quickstart
router = routers.DefaultRouter()
router.register('profiles', views.ProfilePostViewSet)
post_router = routers.NestedDefaultRouter(
    router, 'profiles', lookup='profiles'
)


post_router.register(
    'posts', views.PostViewSet, basename='profile-posts'
)
post_router.register(
    'post-images', views.PostImageViewSet, basename='profile-postimages'
)
post_router.register(
    'post-comments', views.PostCommentViewSet, basename='profile-postcomments'
)


urlpatterns = router.urls + post_router.urls
