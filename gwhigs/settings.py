"""
Django settings for gwhigs project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from __future__ import absolute_import

import os

from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    # Core apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Project apps
    'campaigns',
    'vendors',
    'clients',
    'shows',
    'ads',
    # 3rd party packages
    'grappelli',
    'autocomplete_light',
    'django.contrib.admin',
    'taggit',
    'crispy_forms',
    'floppyforms',
    'simple_history',
    'django_filters',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Simple History pkg functionality
    'simple_history.middleware.HistoryRequestMiddleware',
)

ROOT_URLCONF = 'gwhigs.urls'

WSGI_APPLICATION = 'gwhigs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# End initial settings
# Below were added by Graham

STATIC_URL = '/static/'

# One update needed for django.contrib.messages to play well with Bootstrap 3
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# For use in deployment
# Possibly also STATICFILE_DIRS? e.g.:
#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, "static"),
#    '/var/www/static/',
#)
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

LOGIN_URL = '/login/'

# Grappelli customization
GRAPPELLI_ADMIN_TITLE = 'Performance Bridge Media'

# Crispy-forms customization
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Storages (s3 functionality)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')

AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

# Various other API keys
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

MIDROLL_API_KEY = os.environ.get('MIDROLL_API_KEY')

# Include local settings, if they exists
try:
    from .local_settings import *
except ImportError:
    pass