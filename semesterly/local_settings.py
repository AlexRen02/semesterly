DEBUG = True

TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'aren3',
        'PASSWORD': 'Swimguy1',
        'HOST': 'db',
        'PORT': '5432',
    }
}
