from email.policy import default
from django.db import models

# Create your models here.
class Weapons(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    isStar = models.BooleanField(default='false')
    image = models.ImageField(upload_to='images', null=True, blank=True)