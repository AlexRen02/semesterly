DEBUG = True

TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'semesterly',
        'USER': 'aren3',
        'PASSWORD': 'Swimguy1',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
