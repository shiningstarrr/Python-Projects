from django.db import models
from django.db.models.functions import Now

# Create your models here.
class Emp(models.Model):
    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to = 'images')
    email_address = models.EmailField(max_length = 100, unique = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class items(models.Model):
    name = models.CharField(max_length = 255)
    
