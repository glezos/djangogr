import os, platform

HOME = os.path.dirname(__file__)

DEVELOPMENT_MODE = True

ADMINS = (
    ('Dimitris Glezos','dimitris@glezos.com'),
)
TIME_ZONE = 'Europe/Athens'

SERVER_EMAIL = 'dimitris@glezos.com'

if DEVELOPMENT_MODE:
    DEBUG = True
    PREPEND_WWW = False
    DATABASE_ENGINE = "sqlite3"
    DATABASE_NAME = os.path.join(HOME, "djangogr.sqlite")
    CACHE_BACKEND = 'file://' + os.path.join(HOME, "djangogr_cache/")
    TEMPLATE_DIRS = [os.path.join(HOME, "templates")]
    MEDIA_ROOT = os.path.join(HOME, "media")
    MEDIA_URL = "/media/"
else:
    DEBUG = False
    #PREPEND_WWW = True
    DATABASE_ENGINE = 'sqlite3'
    DATABASE_NAME = os.path.join(HOME, "djangogr.sqlite")
    CACHE_BACKEND = 'file://' + os.path.join(HOME, "djangogr_cache/")
    TEMPLATE_DIRS = [os.path.join(HOME, "templates")]
    MEDIA_ROOT = os.path.join(HOME, "media")
    MEDIA_URL = "http://media.django.gr"

STATIC_SERVE = DEBUG

# Django settings for djangogr project.
TEMPLATE_DEBUG = DEBUG
MANAGERS = ADMINS

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

ADMIN_MEDIA_PREFIX = 'http://www.django.gr/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3zz6@rj_e4am%nk1i1s4udoo#q-96ftjwcv%as9!nct!go5^g)'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'djangogr.urls'

TEMPLATE_DIRS = [os.path.join(HOME, "templates")]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
)
