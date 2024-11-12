1) virtualenvironment
 -  python -m venv django_env
    activate- source django_env/bin/activate -linux
              deactivae
              cd  django_env -windows
              cd Scripts  and activate - windows
              cd Scripts  and deactivate -

aws :- 
 create a user and give s3 bucket full access
 create a acccess keys in local mode crete a s3 bucket
3) download dependeny
   boto3,django-storages
   add 'storages', - in settings - installed apps
4) create a bucket:
    - make it private and create a ploicy to give full acccess to it 
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::django-travel-booking/*"
            }
        ]
    }
    -- cros orgin add this policy it will access to other application 
    [
      {
        "AllowedHeaders":[
            "*"
        ],
        "AllowedMethods":[
             "PUT",
             "POST",
             "GET"
        ],
        "AllowedOrigins":[
            "*"
        ],
        "ExposedHeaders":[]
      }
    ]
5) in settings.py file:- add thes configuration
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


=======================================
added mysql sll key 


===================
test the connections 
python manage.py collectstatic - it copy static file to bucket
python manage.py migrate
python manage.py runserver
