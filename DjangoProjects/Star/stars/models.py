
from django.db import models

# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    isStar = models.BooleanField(default='false')
    image = models.ImageField(upload_to='images', null=True, blank=True)

class Todos(models.Model):
    task = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.task