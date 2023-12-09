from pyexpat import model
from django.db import models

# Create your models here.
class Employee(models.Model): # Automatically create id
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self): # can be displayed in superuser page
        return f"{self.name}, {self.title}"
    
class BlogPosts(models.Model):
    title = models.CharField(max_length=255, null=False,blank=False)
    desc = models.TextField(null=False,blank=False)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self): 
        return f"{self.title}"
