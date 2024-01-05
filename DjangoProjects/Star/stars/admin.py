from django.contrib import admin
from .models import Task,Todo

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display=('task', 'is_completed', 'updated_at')
    search_fields=('task',)

admin.site.register(Task)
admin.site.register(Todo, TaskAdmin)