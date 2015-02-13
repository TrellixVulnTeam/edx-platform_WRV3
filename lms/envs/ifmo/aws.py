from ..aws import *


HTTPS = 'off'

MEDIA_ROOT = '/ifmo/var/uploads'
MEDIA_URL = '/static/uploads/'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

INSTALLED_APPS += (
    'ifmo_mod',
    'ifmo_sso',
    'ifmo_crosscheck',
    'ifmo_edx_static',
    'ifmo_ui',
    'ifmo_stats',
)

