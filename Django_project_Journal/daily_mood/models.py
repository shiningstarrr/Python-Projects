from django.db import models
from django.db.models.functions import Now

# Create your models here.
class timeline(models.Model):
    #date_time = models.DateTimeField(db_default=Now())
    date_added = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
    title = models.CharField(max_length = 255)
    body = models.CharField(max_length = 255)
    is_happy = models.BooleanField()
    image = models.ImageField()
    url = models.SlugField()