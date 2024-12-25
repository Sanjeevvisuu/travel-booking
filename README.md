Your guide on setting up Django with AWS S3 or Azure Blob Storage is clear and comprehensive. Below are a few corrections and improvements to enhance the readability and accuracy of the content, including some fixes for syntax, wording, and clarification:

---

# **Django with AWS S3 or Azure Blob Storage Setup**

This guide explains how to set up a Django project with **AWS S3** or **Azure Blob Storage** for handling static and media files.

## 1. **Set Up Virtual Environment**

Create a virtual environment and activate it:

- **Linux/macOS**:
  ```bash
  python -m venv django_env
  source django_env/bin/activate
  ```

- **Windows**:
  ```bash
  python -m venv django_env
  cd django_env\Scripts
  activate
  ```

- To deactivate the environment:
  ```bash
  deactivate
  ```

---

## 2. **Create IAM Policy (AWS)**

Create an IAM policy for managing access to your S3 bucket:

- **Policy 1 (Basic S3 Access)**:
  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Sid": "AllowPutBucketPolicy",
              "Effect": "Allow",
              "Action": "s3:PutBucketPolicy",
              "Resource": "arn:aws:s3:::my-django-travel-app"
          },
          {
              "Sid": "AllowGetBucketPolicy",
              "Effect": "Allow",
              "Action": "s3:GetBucketPolicy",
              "Resource": "arn:aws:s3:::my-django-travel-app"
          }
      ]
  }
  ```

- **Policy 2 (Full S3 Access)**:
  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "s3:PutBucketPolicy",
                  "s3:PutObject",
                  "s3:GetObject",
                  "s3:ListBucket"
              ],
              "Resource": [
                  "arn:aws:s3:::my-django-travel-app",
                  "arn:aws:s3:::my-django-travel-app/*"
              ]
          }
      ]
  }
  ```

---

## 3. **AWS S3 Setup**

### 3.1. **Create an IAM User**

- Create a new IAM user in the [AWS Management Console](https://aws.amazon.com/iam/).
- Attach the **AmazonS3FullAccess** policy to this user.
- Create **Access Key ID** and **Secret Access Key** for local configuration.

### 3.2. **Create S3 Bucket**

- Go to S3 in the AWS console and create a new bucket (e.g., `django-travel-booking`).
- Set the bucket to **private**.

### 3.3. **Bucket Policy for Public Access (GetObject)**

Add the following policy to allow public read access to objects in the bucket:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-django-travel-app/*"
        }
    ]
}
```

### 3.4. **CORS Policy for Cross-Origin Requests**

Allow cross-origin access to your bucket:

```json
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET",
            "POST",
            "PUT"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```

---

## 4. **Install Dependencies**

Install the required Python packages using pip:

```bash
pip install boto3 django-storages
```

Then, add `storages` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'storages',
    ...
]
```

---

## 5. **Configure AWS S3 in Django Settings**

In your `settings.py`, add the following AWS S3 settings:

```python
import os
from storages.backends.s3boto3 import S3Boto3Storage

# AWS S3 Configuration
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME")
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_ADDRESSING_STYLE = "virtual"
AWS_S3_FILE_OVERWRITE = False

# Static files settings
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files settings
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Storage Configuration
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "LOCATION": "static",  # Path for static files in S3
    },
    "mediafiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "LOCATION": "media",  # Path for media files in S3
    },
}
```

---

## 6. **Azure Blob Storage Setup (Optional)**

If you prefer using **Azure Blob Storage** for static and media files, follow these steps:

### 6.1. **Install Azure Storage Dependency**

In your `requirements.txt`, add the following:

```text
django-storages[azure]
```

### 6.2. **Azure Storage Configuration in `settings.py`**

Add the following Azure Blob Storage configuration:

```python
from storages.backends.azure_storage import AzureStorage

# Azure Storage Configuration
AZURE_CONTAINER_NAME_MEDIA = os.getenv("AZURE_CONTAINER_MEDIA")  # Media container name
AZURE_CONTAINER_NAME_STATIC = os.getenv("AZURE_CONTAINER_STATIC")  # Static container name
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
```

### 6.3. **Create Azure Containers**

1. Create two containers in Azure Blob Storage:
   - **Media Container** (for media files)
   - **Static Container** (for static files)

2. **Set Container Permissions:**
   - Set both containers to **anonymous access** (allow public read access).

---

## 7. **Docker Setup (Optional)**

```bash
# Build and run the Docker containers
docker-compose build
docker-compose up

# After building and running, log into the container to create a superuser
docker exec -it <container_name_or_id> /bin/bash
# or
docker exec -it <container_name_or_id> /bin/sh

# Run Django commands
python manage.py createsuperuser
python manage.py collectstatic
```

---

## 8. **Automate Using Jenkins (Optional)**

To avoid permission issues when using Docker with Jenkins:

```bash
# Add the user to the docker group
sudo usermod -aG docker <your_username>
sudo usermod -aG docker jenkins

# Set permissions on the Docker socket
ls -l /var/run/docker.sock
sudo chown root:docker /var/run/docker.sock
sudo chmod 660 /var/run/docker.sock

# Restart Docker and Jenkins services
sudo systemctl restart docker
sudo systemctl restart jenkins
```

---

### **Summary**

- **AWS S3 Setup**:
  - Create an IAM user with access to S3.
  - Set up an S3 bucket with appropriate policies and CORS configuration.
  - Install `boto3` and `django-storages` for handling static/media files.

- **Azure Blob Storage Setup (Optional)**:
  - Install `django-storages[azure]`.
  - Set up Azure Blob Storage for static and media files.
  - Configure containers for public access.

- **Docker Setup** (Optional):
  - Build and run Docker containers.
  - Create a superuser and collect static files.

This setup will allow you to store and serve static and media files from **AWS S3** or **Azure Blob Storage** in your Django application.

---

