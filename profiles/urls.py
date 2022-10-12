from rest_framework_nested import routers
from connects import views as connects
from follows import views as follows
from . import views


# Guide source:
# https://github.com/alanjds/drf-nested-routers#quickstart
router = routers.DefaultRouter()
router.register('', views.ProfileViewSet)
profile_router = routers.NestedDefaultRouter(
    router, '', lookup='profiles'
)

profile_router.register(
    'linktree', views.LinkViewSet, basename='profile-linktrees'
)
profile_router.register(
    'socials', views.SocialViewSet, basename='profile-socials'
)
profile_router.register(
    'portfolios', views.PortfolioViewSet, basename='profile-portfolios'
)
profile_router.register(
    'awards', views.AwardViewSet, basename='profile-awards'
)
profile_router.register(
    'certificates', views.CertificateViewSet, basename='profile-certificates'
)
profile_router.register(
    'creatives', views.CreativeViewSet, basename='profile-creatives'
)
profile_router.register(
    'settings', views.SettingViewSet, basename='profile-settings'
)

# Connects app routes
profile_router.register(
    'connecter', connects.ConnecterViewSet, basename='profile-connecter'
)
profile_router.register(
    'connecting', connects.ConnectingViewSet, basename='profile-connecting'
)
# Follows app route
profile_router.register(
    'follow', follows.FollowViewSet, basename='profile-follows'
)
profile_router.register(
    'following', follows.FollowingViewSet, basename='profile-following'
)


urlpatterns = router.urls + profile_router.urls
