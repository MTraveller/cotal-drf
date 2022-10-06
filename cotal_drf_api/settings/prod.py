""" Production Settings """
import os
import json
from dotenv import load_dotenv
import dj_database_url
from .common import *


load_dotenv()

DEBUG = False

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('DJANGO_CLOUDINARY_URL')
}

API_ENDPOINT = os.environ.get('API_ENDPOINT')

ALLOWED_HOSTS = [
    host for host in json.loads(
        os.environ['DJANGO_ALLOWED_HOSTS']
    )
]

CORS_ALLOWED_ORIGINS = [
    f"https://{host}" for host in json.loads(
        os.environ['DJANGO_ALLOWED_HOSTS']
    )
]

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
)
