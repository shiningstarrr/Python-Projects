from django.shortcuts import render
from django.http import HttpResponse
from .models import Task,Todo
# Create your views here.

def home(request):
    return render(request, 'home.html')
# def detail(request):
#     tasks = Task.objects.all()
#     context={
#         'tasks':tasks,
#     }
#     return render(request, 'detail.html', context)

def todos(request):
    todos = Todo.objects.filter(is_completed=False)
    finished=Todo.objects.filter(is_completed=True)
    context={
        'todo':todos,
        'finished':finished,
    }
    return render(request, 'detail.html', context)