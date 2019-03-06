import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

"""
DATABASES = {

    'db2': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db2.sqlite3'),
    }
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db',
    },
    'db2': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db2',
    },
}
"""
DEBUG = True
