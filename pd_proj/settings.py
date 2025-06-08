import os
from pathlib import Path
import dj_database_url
# Uncomment for Heroku deployment
import django_heroku

BASE_DIR = Path(__file__).resolve().parent.parent

# Debug prints
print("ENVIRONMENT_CONDITIONZ:", os.environ.get('ENVIRONMENT_CONDITIONZ'))

SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-secret-key-for-testing')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')
ENVIRONMENT_CONDITIONZ = os.environ.get('ENVIRONMENT_CONDITIONZ', 'development')

if ENVIRONMENT_CONDITIONZ == 'development':
    DEBUG = os.environ.get('DEBUG_DEVELOPMENT', 'True') == 'True'
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'core/static')]
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    print('dohick')
elif ENVIRONMENT_CONDITIONZ == 'production':
    DEBUG = os.environ.get('DEBUG_PRODUCTION', 'False') == 'True'
    DO_SPACES_KEY = os.environ.get('DO_SPACES_KEY')
    DO_SPACES_SECRET = os.environ.get('DO_SPACES_SECRET')
    DO_SPACES_BUCKET_NAME = os.environ.get('DO_SPACES_BUCKET_NAME')
    DO_SPACES_REGION = os.environ.get('DO_SPACES_REGION', 'nyc3')
    DO_SPACES_ENDPOINT_URL = f'https://{DO_SPACES_REGION}.digitaloceanspaces.com'
    DO_SPACES_CUSTOM_DOMAIN = f'{DO_SPACES_BUCKET_NAME}.{DO_SPACES_REGION}.cdn.digitaloceanspaces.com'

    AWS_ACCESS_KEY_ID = DO_SPACES_KEY
    AWS_SECRET_ACCESS_KEY = DO_SPACES_SECRET
    AWS_STORAGE_BUCKET_NAME = DO_SPACES_BUCKET_NAME
    AWS_S3_REGION_NAME = DO_SPACES_REGION
    AWS_S3_ENDPOINT_URL = DO_SPACES_ENDPOINT_URL
    AWS_S3_CUSTOM_DOMAIN = DO_SPACES_CUSTOM_DOMAIN
    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = 'public-read'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
    STATIC_ROOT = BASE_DIR / 'staticfiles'  # Add this
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
    STORAGES = {
        'default': {'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage'},
        'staticfiles': {'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage'},
    }
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL')
        )
    }
    print('hickleberrrrries')

ADMIN_URL = os.environ.get('ADMIN')
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

INSTALLED_APPS = [
    'jazzmin',
    'core.apps.CoreConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'item',
    'dashboard',
    'conversation',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pd_proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pd_proj.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Uncomment for Heroku deployment
django_heroku.settings(locals())

JAZZMIN_SETTINGS = {
    'site_title': "Paul's Dogs Admin",
    'site_header': 'Pauls Dogs',
    'site_brand': 'Pauls Dogs',
    'site_logo': 'core/images/pd_logo_02.svg',
    'welcome_sign': 'Welcome to Pauls Dogs!',
    'show_version': False,
    'footer_logo': None,
    'footer_title': 'Pd Project Woof',
    'copyright': 'Pauls Dogs',
    'topmenu_links': [
        {'app': 'core'},
        {'name': 'Home', 'url': 'https://paulsdogs-f1b5116d1567.herokuapp.com/', 'new_window': True},
    ],
    'show_ui_builder': False,
    'custom_css': 'core/css/custom.css',
}

JAZZMIN_UI_TWEAKS = {
    'navbar_small_text': False,
    'footer_small_text': False,
    'body_small_text': False,
    'brand_small_text': False,
    'brand_colour': False,
    'accent': 'accent-primary',
    'navbar': 'navbar-dark',
    'no_navbar_border': False,
    'navbar_fixed': False,
    'layout_boxed': False,
    'footer_fixed': False,
    'sidebar_fixed': True,
    'sidebar': 'sidebar-dark-info',
    'sidebar_nav_small_text': False,
    'sidebar_disable_expand': False,
    'sidebar_nav_child_indent': False,
    'sidebar_nav_compact_style': False,
    'sidebar_nav_legacy_style': False,
    'sidebar_nav_flat_style': False,
    'theme': 'cyborg',
    'dark_mode_theme': None,
    'button_classes': {
        'primary': 'btn-primary',
        'secondary': 'btn-secondary',
        'info': 'btn-info',
        'warning': 'btn-warning',
        'danger': 'btn-danger',
        'success': 'btn-success'
    }
}