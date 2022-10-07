from core.urls import router, profile_router
from . import views

profile_router.register('linktree', views.LinkViewSet,
                        basename='profile-linktrees')
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

urlpatterns = router.urls + profile_router.urls
