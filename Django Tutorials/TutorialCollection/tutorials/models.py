from django.db import models

# Todo App Model
class Task(models.Model):
    task = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.task

class Uploads(models.Model):
    image = models.ImageField(upload_to='images', null=True, blank=True)
    name = models.CharField(max_length = 255)