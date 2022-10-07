from rest_framework_nested import routers
from . import views

# Guide source:
# https://github.com/alanjds/drf-nested-routers#quickstart
router = routers.DefaultRouter()
router.register('profiles', views.ProfileViewSet)

profile_router = routers.NestedDefaultRouter(
    router, 'profiles', lookup='profiles')


# URLConf
urlpatterns = router.urls + profile_router.urls
