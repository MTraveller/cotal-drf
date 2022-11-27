""" Production Settings """
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

API_ENDPOINT = os.environ.get('API_ENDPOINT')

INTERNAL_IPS = [
    "0.0.0.0", "127.0.0.1", "localhost",
]

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

print(CORS_ALLOWED_ORIGINS)

DATABASES = {
    'default': dj_database_url.parse(os.environ['DATABASE_URL'])
}

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
)

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT', 'Cotal',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
}
