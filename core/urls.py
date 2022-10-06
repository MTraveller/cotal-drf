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
profile_router.register('portfolios', views.PortfolioViewSet,
                        basename='profile-portfolios')
profile_router.register('awards', views.AwardViewSet,
                        basename='profile-awards')
profile_router.register('certificates', views.CertificateViewSet,
                        basename='profile-certificates')
profile_router.register('creatives', views.CreativeViewSet,
                        basename='profile-creatives')
profile_router.register('settings', views.SettingViewSet,
                        basename='profile-settings')

# URLConf
urlpatterns = router.urls + profile_router.urls
