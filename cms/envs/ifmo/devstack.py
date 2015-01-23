from ..devstack import *

HTTPS = 'off'

MEDIA_ROOT = '/edx/var/edxapp/uploads'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

INSTALLED_APPS += (
    'ifmo_mod',
    'ifmo_sso',
    'ifmo_crosscheck',
    'ifmo_edx_static',
    'ifmo_ui',
)

FEATURES['ALLOW_ALL_ADVANCED_COMPONENTS'] = True
