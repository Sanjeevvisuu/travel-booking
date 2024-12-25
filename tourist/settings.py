

from pathlib import Path
import os
#environment variable
from dotenv import load_dotenv
load_dotenv()
#connect with aws bucket
from storages.backends.s3boto3 import S3Boto3Storage 
#connect with azure storage
from storages.backends.azure_storage import AzureStorage
# Build paths inside the project like this: BASE_DIR / 'subdir'.

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("djnago_sec_key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #installed apps
    "website_app",
    "product",
    "booking",
    "contact",
    "about_us",
    "payment",
    # third party apps
    'django_filters',
    #connect with aws s3 bucket
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

ROOT_URLCONF = 'tourist.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"template")],
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

WSGI_APPLICATION = 'tourist.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql' ,
        'NAME': os.getenv("DB_name") ,
        'USER': os.getenv("DB_user") ,
        'PASSWORD': os.getenv("DB_passwd"),
        'HOST': os.getenv("DB_host") ,
        'PORT': os.getenv("DB_port"),
      #  'OPTIONS': {
       #          'ssl': {'ca': '/etc/ssl/certs/DigiCertGlobalRootCA.crt.pem'}  # Path to the SSL certificate
       #  },
    } 
}
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#---------------------------------------
#aws s3 bucket

# AWS S3 configuration for static and media files


AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME")
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_ADDRESSING_STYLE = "virtual"
AWS_S3_FILE_OVERWRITE = False

# Static files settings
STATIC_URL = 'static/'  # Static URL
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # when we prith python manage.py collectstatic all the static file will store here

# Media files settings
MEDIA_URL = 'media/'  # Media URL
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Local media directory
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "LOCATION": "static",  # Ensure this matches the path in your bucket
    },
    "mediafiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "LOCATION": "media",  # Ensure this matches the path in your bucket
    },
}

#-------------------------------
"""
# Static files settings
STATIC_URL = 'static/'  # Static URL
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # when we prith python manage.py collectstatic all the static file will store here


#Azure

AZURE_CONTAINER_NAME_MEDIA = os.getenv("AZURE_CONTAINER_MEDIA")  # default media container name
AZURE_CONTAINER_NAME_STATIC = os.getenv("AZURE_CONTAINER_STATIC")  # default static container name
AZURE_ACCOUNT_NAME = os.getenv("AZURE_ACCOUNT_NAME")  # Your Azure account name
AZURE_ACCOUNT_KEY = os.getenv("AZURE_ACCOUNT_KEY")  # Your Azure account key
# Configure django-storages to use Azure Blob Storage for static and media files
DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
STATICFILES_STORAGE = 'storages.backends.azure_storage.AzureStorage'
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.azure_storage.AzureStorage",
        "OPTIONS": {
            "account_name": AZURE_ACCOUNT_NAME,
            "account_key": AZURE_ACCOUNT_KEY,
            "azure_container": AZURE_CONTAINER_NAME_MEDIA,  # Container for media files
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.azure_storage.AzureStorage",
        "OPTIONS": {
            "account_name": AZURE_ACCOUNT_NAME,
            "account_key": AZURE_ACCOUNT_KEY,
            "azure_container": AZURE_CONTAINER_NAME_STATIC,  # Container for static files
        },
    },
}

"""


RAZORPAY_SECRET_KEY=os.getenv("razor_sec_key")
RAZORPAY_PRODUCT_ID=os.getenv("razor_prod_id")
