"""
Django settings for web_conafe project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import socket
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-0fp9evx!mdv3ewu&u@f2nqx07=h5ff$#-7y8$bynzei1*7)zb5"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "login_app",
    "modulo_dot",
    "home_empleado",
    "modulo_coordinador",
    "form_app",
    "widget_tweaks",
    "modulo_apec",
    "modulo_dpe",
    'modulo_DECB',
    'modulo_educadores',
    'modulo_capacitacion',
    'modulo_calendario',
    "corsheaders",    
    'rest_framework'
]
CORS_ALLOW_ALL_ORIGINS = True  # Permite solicitudes desde cualquier dominio
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "web_conafe.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "web_conafe.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# Configuración inicial de las bases de datos
# Configuraciones de bases de datos

# Detectar si la conexión es local o remota
try:
    # Verifica si puedes acceder a la IP pública de Google Cloud
    socket.create_connection(("34.118.149.167", 3306), timeout=1)
    is_online = True
except OSError:
    is_online = False

if is_online:
    # Configuración para Google Cloud
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "HOST": "34.118.149.167",  # IP pública de Google Cloud
            "PORT": "3306",  # Puerto configurado
            "NAME": "conafe_motor",
            "USER": "root",
            "PASSWORD": "1234567890",
        }
    }
    print("Connected a Google Cloud Database")
else:
    # Configuración para base de datos local (ejemplo: MySQL local)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "HOST": "127.0.0.1",  # IP local
            "PORT": "3306",  # Puerto local
            "NAME": "conafe_local",
            "USER": "root",
            "PASSWORD": "1234567890",  # Cambia a tu contraseña local
        }
    }
    print("Connected a Local Database")
# Aquí se definen las bases de datos en settings.py
DATABASES = DATABASES

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS  = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / "staticfiles"


MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "login_app.UsuarioRol"
# Añadir esto en settings.py

LOGIN_URL = "/login/"

LANGUAGE_CODE = 'es'

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
