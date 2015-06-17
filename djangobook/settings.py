"""
Django settings for djangobook project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

TEMPLATE_DIRS = [
	TEMPLATE_PATH,
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '22mbamq2s!dz0q@bhiiwf0#h7h92inxjomoe&&s18nf6@=8l%$'

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
    'simplenation',
    'tinymce',
    #'registration',
    'taggit',
    'snippets',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'djangobook.urls'

WSGI_APPLICATION = 'djangobook.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangobook',
	'USER': 'djangobook',
	'PASSWORD': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = '/Users/timurmalgazhdarov/Sites/djangobook.com/media/'
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = '/Users/timurmalgazhdarov/Sites/djangobook.com/static/'
STATIC_PATH = '/Users/timurmalgazhdarov/Sites/djangobook.com/static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
	STATIC_PATH,
)

TINYMCE_JS_ROOT = os.path.join(STATIC_PATH, 'js/tiny_mce')

TINYMCE_JS_URL = 'http://dev.example.org/static/js/tiny_mce/tiny_mce.js'
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True

# REGISTRATION_OPEN = True       
# ACCOUNT_ACTIVATION_DAYS = 7     
# REGISTRATION_AUTO_LOGIN = True  
# LOGIN_REDIRECT_URL = '/simplenation/'  
# LOGIN_URL = '/accounts/login/'
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/Users/timurmalgazhdarov/Sites/djangobook.com/static/registration/email-messages'

PROFANITY_CHECK_THRESHOLD = 10
