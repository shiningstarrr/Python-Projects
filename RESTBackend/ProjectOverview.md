# Django Rest Framework Project - Introduction
- REST stands for Representational State Transfer Application Programming Interface
- Create Virtual Env: ```py -3 -m venv .venv```
- Add git ignore: .gitignore file
- Install Django: ```python -m pip install Django```
- Update pip: ```python.exe -m pip install --upgrade pip```
- Create project: ```django-admin startproject drf .```
- Start app: ```django-admin startapp rest_api```
- Install django rest framework: ```python -m pip install djangorestframework```

# Resources
- Django REST Framework: https://www.django-rest-framework.org/

# Start Project:
- Go to settings.py: add ```'rest_api','rest_framework',``` app to INSTALLED_APPS

# Serialization
- QuerySet: A collection of objects from your database
- Model Instances: An instance of the class represents one object from that model (which maps to one row of the table in the database)
- Serialization: QuerySet, Model instances -> convert to Native Python Datatype -> convert to JSON, XML, or other content Type

# Create the model
- Create Post model in models.py with title, author, and email
- Make migration: ```python manage.py makemigrations``` and ```python manage.py migrate```
- Create superuser: ```python manage.py createsuperuser```

# Register the model
- ```admin.site.register(Post)```