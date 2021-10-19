from back.settings import *
import dj_database_url


DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['backend-kairos.herokuapp.com']

DATABASES['default'] = dj_database_url.config()

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

