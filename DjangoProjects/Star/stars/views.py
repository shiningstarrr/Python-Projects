from django.shortcuts import render
from django.http import HttpResponse
from .models import Tasks
# Create your views here.

def home(request):
    return render(request, 'home.html')
def detail(request):
    tasks = Tasks.objects.all()
    context={
        'tasks':tasks,
    }
    return render(request, 'detail.html', context)
