import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db',
        'USER': 'root',
    },
    'db2': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db2',
        'USER': 'root',
    },
}

DEBUG = True
