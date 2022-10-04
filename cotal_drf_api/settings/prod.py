""" Production Settings """
import os
import dj_database_url
from .common import *

DEBUG = False

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'SAMEORIGIN'

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ('DJANGO_CLOUDINARY_URL')
}

ALLOWED_HOSTS = [
    'https://cotal.vercel.app',
]

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
