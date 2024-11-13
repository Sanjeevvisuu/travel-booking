FROM python:alpine 

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


#creating a directry and make it as working directry
RUN mkdir /my_code
WORKDIR /my_code

#coping files from loacal to container
COPY requirements.txt requirements.txt

#installing dependency packages
# mysql tools 
RUN apk update && apk add --no-cache gcc musl-dev libffi-dev python3-dev pkgconfig mariadb-dev
# from requirements.txt file
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir  -r requirements.txt


#copy all fikes 
COPY . /my_code

# Copy the SSL certificate into the container
COPY certs/DigiCertGlobalRootCA.crt.pem /etc/ssl/certs/
# Update the CA certificates so the system can use the SSL certificate
RUN update-ca-certificates

# Run Django migrations 
RUN python manage.py makemigrations && python manage.py migrate
# Set environment variables from the .env file for the superuser creation
COPY .env /my_code/.env
#to copy static & media  files 
RUN python manage.py collectstatic --noinput


#RUN python manage.py createsuperuser --username adminuser --email adminuser@gmail.com --password adminuser

EXPOSE 8008
CMD ["python", "manage.py", "runserver", "0.0.0.0:8008"]
