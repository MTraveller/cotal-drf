""" Development Settings """
from .common import *

DEBUG = True

# Generate a new django secret key at:
# https://django-secret-key-generator.netlify.app
SECRET_KEY = ''

os.environ.setdefault(
    'CLOUDINARY_URL', ''
)

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

INTERNAL_IPS = [
    "127.0.0.1",
]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

# Un-comment the below to check render as production
# REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
#     'rest_framework.renderers.JSONRenderer',
# )

os.environ.setdefault('API_ENDPOINT', 'api/')

API_ENDPOINT = os.environ.get('API_ENDPOINT')
