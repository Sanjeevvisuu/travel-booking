Here’s a revised version of the guide, optimized for inclusion in a GitHub README file. It’s been reformatted with clearer sections, concise bullet points, and improved readability:

---

# **Django with AWS S3 or Azure Blob Storage Setup**

This guide demonstrates how to configure a Django project to use **AWS S3** or **Azure Blob Storage** for managing static and media files.

---

## **1. Set Up Virtual Environment**

### Linux/macOS:
```bash
python -m venv django_env
source django_env/bin/activate
```

### Windows:
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

## **2. AWS S3 Setup**

### 2.1 Create an IAM User
1. Go to the [AWS Management Console](https://aws.amazon.com/iam/).
2. Create a new IAM user with the **AmazonS3FullAccess** policy.
3. Generate **Access Key ID** and **Secret Access Key** for local configuration.

### 2.2 Create an S3 Bucket
1. Navigate to **S3** in the AWS Console.
2. Create a new bucket (e.g., `django-travel-booking`).

### 2.3 Bucket Policy
Set up the **bucket policy** to allow public read access to objects stored in the bucket.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::YOUR-BUCKET-NAME/*"
        }
    ]
}
```

### 2.4 CORS Configuration
Configure **CORS** to allow cross-origin requests:

```json
[
    {
        "AllowedHeaders": ["*"],
        "AllowedMethods": ["PUT", "POST", "GET"],
        "AllowedOrigins": ["*"],
        "ExposeHeaders": []
    }
]
```

---

## **3. Install Dependencies**

Install the necessary Python packages:
```bash
pip install boto3 django-storages
```

Add `storages` to your `INSTALLED_APPS` in `settings.py`:
```python
INSTALLED_APPS = [
    ...
    'storages',
    ...
]
```

---

## **4. Configure AWS S3 in Django Settings**

In `settings.py`, add the following configurations for AWS S3:

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
        "LOCATION": "static",  # Static file path in S3
    },
    "mediafiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "LOCATION": "media",  # Media file path in S3
    },
}
```

---

## **5. Azure Blob Storage Setup (Optional)**

If you prefer **Azure Blob Storage** over AWS S3, follow these steps:

### 5.1 Install Azure Storage Dependency
Add `django-storages[azure]` to your `requirements.txt`:
```text
django-storages[azure]
```

### 5.2 Azure Storage Configuration in `settings.py`
Update `settings.py` for Azure Blob Storage:

```python
from storages.backends.azure_storage import AzureStorage

# Azure Storage Configuration
AZURE_CONTAINER_NAME_MEDIA = os.getenv("AZURE_CONTAINER_MEDIA")
AZURE_CONTAINER_NAME_STATIC = os.getenv("AZURE_CONTAINER_STATIC")
AZURE_ACCOUNT_NAME = os.getenv("AZURE_ACCOUNT_NAME")
AZURE_ACCOUNT_KEY = os.getenv("AZURE_ACCOUNT_KEY")

# Configure django-storages to use Azure Blob Storage
DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
STATICFILES_STORAGE = 'storages.backends.azure_storage.AzureStorage'

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.azure_storage.AzureStorage",
        "OPTIONS": {
            "account_name": AZURE_ACCOUNT_NAME,
            "account_key": AZURE_ACCOUNT_KEY,
            "azure_container": AZURE_CONTAINER_NAME_MEDIA,  # Media container
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.azure_storage.AzureStorage",
        "OPTIONS": {
            "account_name": AZURE_ACCOUNT_NAME,
            "account_key": AZURE_ACCOUNT_KEY,
            "azure_container": AZURE_CONTAINER_NAME_STATIC,  # Static container
        },
    },
}
```

### 5.3 Create Azure Containers
1. Create two containers in Azure Blob Storage:
   - **Media Container** (for media files)
   - **Static Container** (for static files)
   
2. Set both containers to **anonymous access** for public read access.

---

## **6. Docker Setup (Optional)**

To deploy with Docker, follow these steps:

### 6.1 Build and Run Docker Containers
```bash
docker-compose build
docker-compose up
```

### 6.2 Create Superuser and Collect Static Files
Inside the running container, create a superuser and collect static files:
```bash
docker exec -it <container_name_or_id> /bin/bash
# or
docker exec -it <container_name_or_id> /bin/sh

# Run Django commands
python manage.py createsuperuser
python manage.py collectstatic
```

---

## **7. Jenkins Automation (Optional)**

To resolve Docker permission issues in Jenkins, follow these steps:

```bash
# Add user to the Docker group
sudo usermod -aG docker <your_username>
sudo usermod -aG docker jenkins

# Set permissions on the Docker socket
sudo chown root:docker /var/run/docker.sock
sudo chmod 660 /var/run/docker.sock

# Restart Docker and Jenkins services
sudo systemctl restart docker
sudo systemctl restart jenkins
```

### Connect with AWS EKS Cluster
1. Run `aws configure` to configure AWS CLI.
2. Connect to your EKS cluster:
   ```bash
   aws eks --region <region> update-kubeconfig --name <clustername>
   ```
3. Switch to Jenkins user:
   ```bash
   sudo -su jenkins
   cd /var/lib/jenkins/
   aws configure
   aws eks --region <region> update-kubeconfig --name <clustername>
   ```

---

## **Summary**

- **AWS S3 Setup**:
  - Create an IAM user with S3 access.
  - Set up an S3 bucket with public read access and CORS.
  - Install and configure `boto3` and `django-storages`.

- **Azure Blob Storage Setup (Optional)**:
  - Install `django-storages[azure]`.
  - Set up Azure Blob Storage for static and media files.
  - Configure containers for public access.

- **Docker Setup (Optional)**:
  - Build and run Docker containers.
  - Create a superuser and collect static files.

This setup enables you to store and serve static and media files from **AWS S3** or **Azure Blob Storage** in your Django project.

--- 

