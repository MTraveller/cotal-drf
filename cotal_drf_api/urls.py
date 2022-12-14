"""cotal_drf_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os
from django.conf import settings
from django.contrib import admin
from django.urls import path, include


from . import views


admin.site.site_header = 'Cotal DRF Admin'
admin.site.index_title = 'Admin'

patterns = ([
    path('', views.api_start_endpoint),  # type: ignore
    path('profiles/', include('profiles.urls')),
    path('posts/', include('posts.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('admin/', admin.site.urls),
])

urlpatterns = [
    path('', views.api_root),  # type: ignore
    path(settings.API_ENDPOINT, include(patterns)),
]

if 'dev' in os.environ.get('DJANGO_SETTINGS_MODULE'):  # type: ignore
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls'))
    ] + urlpatterns
