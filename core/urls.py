from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('profiles/', views.profile_list),
    path('profiles/<int:id>', views.profile_detail),
]
