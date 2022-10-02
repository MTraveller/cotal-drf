"""
ASGI config for cotal_drf_api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.user.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cotal_drf_api.settings.dev')

application = get_asgi_application()
