from django.contrib import admin
from .models import Task,Todo

# Register your models here.
admin.site.register(Task)
admin.site.register(Todo)