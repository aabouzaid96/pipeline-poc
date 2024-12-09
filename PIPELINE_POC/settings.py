import os
from pathlib import Path

from tutorial.settings import BASE_DIR


ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'PIPELINE_POC.urls'
DEBUG = True
SECRET_KEY = ')in4_vc0h2*29pq=4zvp!)f7+bjgs38&3e+cei$%=4zvphaez&'
AUTH_USER_MODEL = 'accounts.User'


INSTALLED_APPS = [
    # other apps
    'django.contrib.admin',  # Required for the admin interface
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # For REST APIs

    'accounts',
    # 'Repo-A.add_users',
    # 'Repo-B.delete_users',

]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',  # This must come before AuthenticationMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='pipeline_POC'),  # Database name
        'USER': config('DB_USER', default='postgres'),  # Database username
        'PASSWORD': config('DB_PASSWORD', default='postgres'),  # Database password
        'HOST': 'localhost',  # Local database
        'PORT': config('DB_PORT', default='5432'),  # Database port
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Add your custom templates directory here
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required by the admin app
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Static files (CSS, JavaScript, Images)
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = '/static/'
