from rest_framework_nested import routers
from . import views


# Guide source:
# https://github.com/alanjds/drf-nested-routers#quickstart
router = routers.DefaultRouter()
router.register('profiles', views.ProfileViewSet)
post_router = routers.NestedDefaultRouter(
    router, 'profiles', lookup='profiles'
)


post_router.register(
    'posts', views.PostViewSet, basename='profile-posts'
)


urlpatterns = router.urls + post_router.urls
