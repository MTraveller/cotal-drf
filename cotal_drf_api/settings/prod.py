""" Production Settings """
import os
import dj_database_url
from .common import *

DEBUG = os.environ.get('DEBUG')

# SECURE_SSL_REDIRECT = True

# SESSION_COOKIE_SECURE = True

# CSRF_COOKIE_SECURE = True

# X_FRAME_OPTIONS = 'SAMEORIGIN'

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('DJANGO_CLOUDINARY_URL')
}

print(os.environ.get('DJANGO_ALLOWED_HOSTS'))
ALLOWED_HOSTS = os.environ.list('DJANGO_ALLOWED_HOSTS')

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
