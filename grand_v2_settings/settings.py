from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path( __file__ ).resolve( ).parent.parent

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Read secret and debug settings from environment for production safety.
SECRET_KEY = os.environ.get(
  'DJANGO_SECRET_KEY',
  'django-insecure-development-fallback-change-me'
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

# Allow configuring allowed hosts via environment variable (comma-separated)
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Optional: CSRF trusted origins (comma-separated), useful when using a domain
CSRF_TRUSTED_ORIGINS = (
  os.environ.get('DJANGO_CSRF_TRUSTED_ORIGINS', '')
  .split(',')
  if os.environ.get('DJANGO_CSRF_TRUSTED_ORIGINS')
  else []
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join( BASE_DIR, 'staticfiles' )

STATICFILES_DIRS = [
  os.path.join( BASE_DIR, 'static' ),
  # ... other directories if needed
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join( BASE_DIR, 'media' )

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django_extensions',
  'grand_v2_app',
]

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'grand_v2_settings.urls'

TEMPLATES = [
  {
    'BACKEND' : 'django.template.backends.django.DjangoTemplates',
    'DIRS'    : [ BASE_DIR / 'templates' ],
    'APP_DIRS': True,
    'OPTIONS' : {
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        'grand_v2_app.context_processors.media_url',
      ],
    },
  },
]

WSGI_APPLICATION = 'grand_v2_settings.wsgi.application'

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME'  : BASE_DIR / 'db.sqlite3',
  }
}

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000  # or a higher number, as needed

# DATABASES = {
#   'default': {
#     'ENGINE'  : 'django.db.backends.postgresql',  # Or 'django.db.backends.postgresql_psycopg2'
#     'NAME'    : 'grand_v2_pgdb',
#     'USER'    : 'postgres',
#     'PASSWORD': 'postgres',
#     'HOST'    : 'localhost',  # Or the IP address of your PostgreSQL server
#     'PORT'    : '5432',
#   }
# }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# CRISPY_TEMPLATE_PACK = 'uni_form'
# CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap3"
# CRISPY_TEMPLATE_PACK = "bootstrap3"

# email configuration settings
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'dtebar@gmail.com'
# EMAIL_HOST_PASSWORD = 'gaml xvnn vaar nyvy'
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'dtebar@top-quarks.com'

# email configuration settings
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'dtebar@gmail.com'
# EMAIL_HOST_PASSWORD = 'qjjw mcay bqgi vvbt'
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'dtebar@top-quarks.com'
