"""
Django settings for DownloadvideoWeb project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import yaml

yaml_f = open("./config.yaml", "r", encoding="utf-8")
config_yaml = yaml.load(yaml_f, Loader=yaml.FullLoader)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-6v-!#es%t9fujiw=(ed0rb!jb++8mbz)o6j*^c01j%=z!pvsgp"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 'sqlalchemy_django_admin',
    "flow_tk.apps.TkflowConfig",
    "sqlalchemy",
    "custom",
    "flow_clip_talk.apps.CliptalkConfig",
    "imaotai.apps.ImaotaiConfig"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # 'django.middleware.csrf.CsrfViewMiddleware',
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "DownloadvideoWeb.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "html"],
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

WSGI_APPLICATION = "DownloadvideoWeb.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config_yaml["server_settings"]["MYSQL_DB"],
        "USER": config_yaml["mysql_settings"]["MYSQL_USER"],
        "PASSWORD": config_yaml["mysql_settings"]["MYSQL_PASSWORD"],
        "HOST": config_yaml["mysql_settings"]["MYSQL_HOST"],
        "PORT": config_yaml["mysql_settings"]["MYSQL_PORT"],
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# server_settings
server_url = config_yaml["server_settings"]["url"]

# mysql_settings
MYSQL_DBNAME = config_yaml["mysql_settings"]["MYSQL_DB"]
MYSQL_USER = config_yaml["mysql_settings"]["MYSQL_USER"]
MYSQL_PASSWORD = config_yaml["mysql_settings"]["MYSQL_PASSWORD"]
MYSQL_HOST = config_yaml["mysql_settings"]["MYSQL_HOST"]
MYSQL_PORT = config_yaml["mysql_settings"]["MYSQL_PORT"]

APPEND_SLASH = False
AMAP_KEY = config_yaml["AMAP_KEY"]