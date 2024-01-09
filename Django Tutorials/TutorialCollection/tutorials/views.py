from django.shortcuts import render

from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import Task
# Create your views here.
def home(request):
    return render(request, 'test.html')