import os
from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': config('DB_HOST'),
        'PORT': '5434',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', cast=bool)

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True
USE_TZ = True
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru-ru'
