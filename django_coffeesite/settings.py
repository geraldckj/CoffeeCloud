"""
Django settings for django_coffeesite project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bud%s%zf($6lae8z)h=-rfj&urihkb=r()-cgfm(8%9xc0&ui#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'chartjs',
    'rest_framework',
    'users.apps.UsersConfig',
    'crispy_forms',
    'coffeeCloud.apps.coffeeCloudConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # 'django.contrib.sites.models.Site

    # local


    # allauth for social login
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # providers
    # 'allauth.socialaccounts.providers.facebook',
    'allauth.socialaccount.providers.google',


]

MIDDLEWARE = [
    'crum.CurrentRequestUserMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',

]

ROOT_URLCONF = 'django_coffeesite.urls'

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

WSGI_APPLICATION = 'django_coffeesite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_ROOT = r"C:\Users\geral\Desktop\NU\Coffee Site\venv\django_coffeesite\coffeeCloud\static\coffeeCloud"
STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#     r"C:\Users\geral\Desktop\NU\Coffee Site\venv\django_coffeesite\coffeeCloud\static\coffeeCloud",
#     # "/coffeeCloud/static",
#     # "/coffeeCloud/static/coffeeCloud/main.css",
#     # "/coffeeCloud/static/coffeeCloud/autofill.js",
#     # "/coffeeCloud/static/coffeeCloud/tags.js",
#     # "/coffeeCloud/static/coffeeCloud/formTags.js",
#     # "/coffeeCloud/static/coffeeCloud/tags.css",
#     #
#     # # # bootstrap tokenfield static files
#     # # "venv/django_coffeesite/coffeeCloud/static/coffeeCloud/tkenField_BS/css/bootstrap-tokenfield.css",
#     # # "venv/django_coffeesite/coffeeCloud/static/coffeeCloud/tkenField_BS/bootstrap-tokenfield.js",
#     #
#     # #slideshow static files
#     # "coffeeCloud/static/coffeeCloud/slideshow.js",
#     ]


CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'coffeeCloud-home'

SITE_ID = 1

# Email settings

SERVER_EMAIL = 'leeszeray@outlook.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.outlook.com'
EMAIL_HOST_PASSWORD = 'Stingray2019Y'
EMAIL_HOST_USER = SERVER_EMAIL
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

ADMINS = [
    ('lee', 'leeszeray@outlook.com'),
    # ('gerald', 'geraldckj@gmail.com'),
]

MANAGERS = ADMINS
