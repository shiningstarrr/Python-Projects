from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    email = models.EmailField(default = '')