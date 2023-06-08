from config.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SECRET_KEY = 'django-insecure-x3hca8q@6lavbm^&+2-@g*sr3z%=!ks1!u*o8#^e^dxiw22yg^'

DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'compressor',
    'robots',
    'captcha',
    'home',
    'blog',
    'advertisment',
    'accounts',
]

SITE_ID = 5

COMPRESS_ENABLED = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATIC_ROOT = BASE_DIR.joinpath('/static')
MEDIA_ROOT = BASE_DIR.joinpath('media/')

STATICFILES_DIRS = [
    BASE_DIR/'static',
    BASE_DIR/'media',
]


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
AUTH_USER_MODEL = 'accounts.CustumUser'