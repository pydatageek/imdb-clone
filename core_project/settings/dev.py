from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # debug_toolbar for debug=True
]

# debug_toolbar for debug=True
INTERNAL_IPS = [
    '127.0.0.1',
]
