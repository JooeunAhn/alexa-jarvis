from .common import *
from .secret import DB_USER, DB_PASSWORD

DEBUG = False

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, "..", "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, "..", "media")

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DJANGO_DATABASE_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': os.environ.get('DJANGO_DATABASE_NAME', 'ubuntu'),
        'USER': os.environ.get('DJANGO_DATABASE_USER', DB_USER),
        'PASSWORD': os.environ.get('DJANGO_DATABASE_PASSWORD', DB_PASSWORD),
        'HOST': os.environ.get('DJANGO_DATABASE_HOST', '127.0.0.1'),
    }
}
