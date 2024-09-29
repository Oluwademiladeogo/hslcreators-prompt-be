"""
Django settings for PromptBE project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

import dj_database_url
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# Load environment variables from .env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'rest_framework_swagger',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    'channels',
    'drf_yasg',
    
    'apps.authentication',
    'apps.core',
    'apps.orders',
    'apps.wallet',
    'apps.reviews',
    'apps.notifications',
    
]

REST_FRAMEWORK = { 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema' }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

CORS_ALLOW_HEADERS = [
    'x-api-key',
    'content-type',
    'X-CSRFToken',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    
    "http://prompt.vercel.app",
    "https://prompt.vercel.app",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    
    "http://prompt.vercel.app",
    "https://prompt.vercel.app",

    "http://promptbe.onrender.com",
    "https://promptbe.onrender.com",

    "http://prompt-be-production.up.railway.app",
    "http://prompt-be-production.up.railway.app"
]

CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'PromptBE.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'PromptBE.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(config("DATABASE_URL"))
}

# Custom User Model
AUTH_USER_MODEL = 'authentication.User'


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# MEDIA
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# EMAIL settings
# EMAIL_BACKEND = f'{config('EMAIL_BACKEND')}'
# EMAIL_HOST = f'{config('EMAIL_HOST')}'
# EMAIL_PORT = f'{config('EMAIL_PORT')}'  # or the appropriate port
# EMAIL_USE_TLS = f'{config('EMAIL_USE_TLS')}'
# EMAIL_HOST_USER = f'{config('EMAIL_HOST_USER')}'
# EMAIL_HOST_PASSWORD = f'{config('EMAIL_HOST_PASSWORD')}'
