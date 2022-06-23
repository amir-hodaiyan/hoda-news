import os
import math
import captcha
from pathlib import Path
from decouple import config
# from .security_config import *
from django.utils.translation import gettext_lazy as _

SECRET_KEY = config('SECRET_KEY')
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'modeltranslation',
    'django_otp',
    'django_otp.plugins.otp_totp',
    'widget_tweaks',
    'star_ratings',
    'captcha',

    'account.apps.AccountConfig',
    'home.apps.HomeConfig',
    'employee.apps.EmployeeConfig',
    'photo.apps.PhotoConfig',
    'video.apps.VideoConfig',
    'news.apps.NewsConfig',
    'contact_us.apps.ContactUsConfig',
    'base.apps.BaseConfig',
    'comment.apps.CommentConfig',
]
BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Translate
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    # Custom  middleware
    'home.middleware.VisitPostCounterMiddleware',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': 1,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'base.context_processors.post',  # custom

            ],
        },
    },
]
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'sqlite3.db',
    }
}

LANGUAGES = (('en', _('English')), ('fa', _('Persian')))
LANGUAGE_CODE = 'en'
USE_I18N = True

TIME_ZONE = 'Asia/Tehran'
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'static'

LOGOUT_REDIRECT_URL = 'Home:home'
LOGIN_REDIRECT_URL = 'Home:home'
LOGIN_URL = 'Account:login'
# config for CAPTCHA
CAPTCHA_FONT_SIZE = 38
CAPTCHA_IMAGE_SIZE = (170, 55)
CAPTCHA_LETTER_ROTATION = (-45, 45)
CAPTCHA_TIMEOUT = 2
CAPTCHA_LENGTH = 5
# ------- END ---------------
EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')

# ------- Deploy config ---------------
DEBUG = 1
ALLOWED_HOSTS = ['*']
