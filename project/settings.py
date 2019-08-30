import os
from decouple import config
import sys

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

if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'HOST': 'localhost',
            'NAME': os.path.join(os.path.dirname(__file__), 'test.db'),
            'TEST_NAME': os.path.join(os.path.dirname(__file__), 'test.db'),
        }
    }

    INSTALLED_APPS = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'datacenter',
    ]

    # SOUTH_TESTS_MIGRATE = False
