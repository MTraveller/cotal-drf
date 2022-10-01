from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('profiles', views.ProfileViewSet)
router.urls

# URLConf
urlpatterns = router.urls
