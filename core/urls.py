from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('profiles', views.ProfileViewSet)

profiles_router = routers.NestedDefaultRouter(
    router, 'profiles', lookup='profile')
profiles_router.register('links', views.LinkViewSet, basename='profile-links')
profiles_router.register('socials', views.SocialViewSet,
                         basename='profile-socials')

# URLConf
urlpatterns = router.urls + profiles_router.urls
