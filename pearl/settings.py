"""
Django settings for pearl project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'templates/registration'),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@-+a#8cz=$*c^&jjf9ai!cw976%k!+@v3!%l+j9e%-d#h466*i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #'django.contrib.sites',
    'registration',
    'home',
)


# django-passwords
PASSWORD_MIN_LENGTH = 8
PASSWORD_COMPLEXITY = { # You can ommit any or all of these for no limit for that particular set
    "UPPER": 1,       # Uppercase
    "LOWER": 1,       # Lowercase
    "DIGITS": 1,      # Digits
    #"NON ASCII": 1,   # Non Ascii (ord() >= 128)
    "PUNCTUATION": 1, # Punctuation (string.punctuation)
}


# django-registration - testing
ACCOUNT_ACTIVATION_DAYS = 7
"""
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'testing@example.com'
"""
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'nandapk0@gmail.com'
EMAIL_HOST_PASSWORD = 'nandapk1'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pearl.urls'

WSGI_APPLICATION = 'pearl.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
