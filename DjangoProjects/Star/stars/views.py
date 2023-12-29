from django.shortcuts import render
from django.http import HttpResponse
from .models import Weapons
# Create your views here.

def home(request):
    weapons = Weapons.objects.all()
    context={
        'weapons':weapons,
    }
    return render(request, 'home.html',context)
