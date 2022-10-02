from django.urls import path
from rest_framework_nested import routers
from . import views

# Guide source:
# https://github.com/alanjds/drf-nested-routers#quickstart
router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet)

profile_router = routers.NestedDefaultRouter(
    router, 'profile', lookup='profile')
profile_router.register('links', views.LinkViewSet, basename='profile-links')
profile_router.register('socials', views.SocialViewSet,
                        basename='profile-socials')

# URLConf
urlpatterns = router.urls + profile_router.urls
