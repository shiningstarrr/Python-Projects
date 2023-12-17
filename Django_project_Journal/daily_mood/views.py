from django.http import HttpResponse
from django.shortcuts import render
from .models import Current, Emp


# Create your views here.
def home(request):
    e = Emp.objects.all()
    i = Current.objects.all()
    context = {
        "emp":e,
        "current":i
    }
    return render(request, 'homePage.html',context)

