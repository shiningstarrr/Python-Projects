from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import Task

# For testing:
def appList(request):
    return render(request, 'home.html')

# Log-in Page:
def login(request):
    return render(request,'login.html')

# Todo App Methods:
def list_todos(request):
    unfinished = Task.objects.filter(is_completed = False).order_by('-updated_at')
    finished=Task.objects.filter(is_completed=True)
    context={
        'unfinished':unfinished,
        'finished':finished,
    }
    return render(request, 'todoAppMain.html', context)