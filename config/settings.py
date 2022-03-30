"""
Django settings for dora project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import random
from datetime import timedelta
from pathlib import Path

import dj_database_url
import sentry_sdk
from corsheaders.defaults import default_headers
from sentry_sdk.integrations.django import DjangoIntegration

random.seed()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

if os.path.isdir(BASE_DIR / "envs"):
    import environ

    environ.Env.read_env(os.path.join(BASE_DIR / "envs", "dev.env"))
    environ.Env.read_env(os.path.join(BASE_DIR / "envs", "secrets.env"))


ENVIRONMENT = os.environ["ENVIRONMENT"]


if os.environ["ENVIRONMENT"] != "local":
    sentry_sdk.init(
        dsn=os.environ["SENTRY_DSN"],
        integrations=[DjangoIntegration()],
        traces_sample_rate=0,
        send_default_pii=True,
        environment=os.environ["ENVIRONMENT"],
    )


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ["DJANGO_DEBUG"] == "true"

# DJANGO_ADMINS=Name1:email1,Name2:email2
ADMINS = (
    [u.split(":") for u in os.environ["DJANGO_ADMINS"].split(",")]
    if os.environ.get("DJANGO_ADMINS")
    else None
)

ALLOWED_HOSTS = (
    os.environ["DJANGO_ALLOWED_HOSTS"].split(",")
    if os.environ.get("DJANGO_ALLOWED_HOSTS")
    else None
)

# Application definition

INSTALLED_APPS = [
    "django.contrib.gis",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "django_filters",
    "rest_framework",
    "rest_framework_gis",
    "corsheaders",
    "drf_spectacular",
    # local
    "config.apps.AdminConfig",
    "dora.core",
    "dora.rest_auth",
    "dora.users",
    "dora.structures",
    "dora.services",
    "dora.service_suggestions",
    "dora.sirene",
    "dora.admin_express",
    "dora.stats",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "csp.middleware.CSPMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "dora.core.context_processors.environment",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

try:
    database_url = os.environ["DATABASE_URL"]
    DATABASES = {"default": dj_database_url.config(ssl_require=True)}
    DATABASES["default"]["ENGINE"] = "django.contrib.gis.db.backends.postgis"
except KeyError:
    DATABASES = {
        "default": {
            "ENGINE": "django.contrib.gis.db.backends.postgis",
            "NAME": os.environ["POSTGRES_DB"],
            "USER": os.environ["POSTGRES_USER"],
            "PASSWORD": os.environ["POSTGRES_PASSWORD"],
            "HOST": os.environ["POSTGRES_HOST"],
            "PORT": os.environ["POSTGRES_PORT"],
        }
    }


AUTH_USER_MODEL = "users.User"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        "OPTIONS": {
            "user_attributes": ["first_name", "last_name", "email"],
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 9,
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "fr-fr"

TIME_ZONE = "Europe/Paris"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


# User uploaded files
# https://django-storages.readthedocs.io/en/latest/backends/azure.html
DEFAULT_FILE_STORAGE = "storages.backends.azure_storage.AzureStorage"
AZURE_ACCOUNT_NAME = os.environ["AZURE_ACCOUNT_NAME"]
AZURE_ACCOUNT_KEY = os.environ["AZURE_ACCOUNT_KEY"]
AZURE_CONTAINER = os.environ["AZURE_CONTAINER"]
AZURE_URL_EXPIRATION_SECS = 24 * 3600

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Rest Framework
# https://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {
    # Let's lock down access by default
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAdminUser",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "dora.rest_auth.authentication.TokenAuthentication",
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    # Camel Case
    # https://github.com/vbabiy/djangorestframework-camel-case
    "DEFAULT_RENDERER_CLASSES": (
        "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
    ),
    "DEFAULT_PARSER_CLASSES": (
        "djangorestframework_camel_case.parser.CamelCaseFormParser",
        "djangorestframework_camel_case.parser.CamelCaseMultiPartParser",
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
    ),
    "JSON_UNDERSCOREIZE": {
        "no_underscore_before_number": True,
    },
    "EXCEPTION_HANDLER": "dora.core.exceptions_handler.custom_exception_handler",
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# CORS
# https://github.com/adamchainz/django-cors-headers/blob/main/README.rst

CORS_ALLOWED_ORIGIN_REGEXES = [os.environ["DJANGO_CORS_ALLOWED_ORIGIN_REGEXES"]]

CORS_ALLOW_HEADERS = list(default_headers) + [
    "sentry-trace",
]

##################
# EMAIL SETTINGS #
##################
DEFAULT_FROM_EMAIL = os.environ["DEFAULT_FROM_EMAIL"]

# https://app.tipimail.com/#/app/settings/smtp_and_apis

EMAIL_HOST = os.environ["EMAIL_HOST"]
EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]
EMAIL_SUBJECT_PREFIX = os.environ["EMAIL_SUBJECT_PREFIX"]
EMAIL_PORT = os.environ["EMAIL_PORT"]
EMAIL_USE_TLS = True
EMAIL_DOMAIN = os.environ["EMAIL_DOMAIN"]
FRONTEND_URL = os.environ["FRONTEND_URL"]
SUPPORT_EMAIL = os.environ["SUPPORT_EMAIL"]

INVITATION_LINK_EXPIRATION = timedelta(days=15)
AUTH_LINK_EXPIRATION = timedelta(days=1)

################
# APP SETTINGS #
################

# Services
DEFAULT_SEARCH_RADIUS = 15  # in km

# Bot user
DORA_BOT_USER = "dora-bot@dora.beta.gouv.fr"

# Third party credentials

PE_CLIENT_ID = os.environ["PE_CLIENT_ID"]
PE_CLIENT_SECRET = os.environ["PE_CLIENT_SECRET"]

MATTERMOST_HOOK_KEY = os.environ.get("MATTERMOST_HOOK_KEY")

################
# SECURITY     #
################
if not DEBUG:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    # Disabled as this is already managed by Scalingo
    # SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    # https://hstspreload.org/
    # SECURE_HSTS_PRELOAD = True
    SECURE_REFERRER_POLICY = "same-origin"
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_SSL_REDIRECT = True

PUBLIC_API_VERSIONS = ["1"]

CSP_EXCLUDE_URL_PREFIXES = tuple(
    f"/api/v{version}/schema/doc/" for version in PUBLIC_API_VERSIONS
)

###################
# DRF-SPECTACULAR #
###################
SPECTACULAR_SETTINGS = {
    "TITLE": "API référentiel de l’offre d’insertion",
    "DESCRIPTION": "",
    "VERSION": None,
    "CAMELIZE_NAMES": False,
    "POSTPROCESSING_HOOKS": [
        "drf_spectacular.hooks.postprocess_schema_enums",
        "drf_spectacular.contrib.djangorestframework_camel_case.camelize_serializer_fields",
    ],
    "SORT_OPERATIONS": False,
    "SERVE_INCLUDE_SCHEMA": False,
    "COMPONENT_NO_READ_ONLY_REQUIRED": True,
}
