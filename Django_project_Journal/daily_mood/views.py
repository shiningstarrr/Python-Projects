from django.http import HttpResponse
from django.shortcuts import render
from .models import Emp

# Create your views here.
def home(request):
    e = Emp.objects.all()
    context = {
        "emp":e
    }
    return render(request, 'homePage.html',context)
