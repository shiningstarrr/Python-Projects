from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Employee

# Create your views here.
def index(request):
    myEmployees = Employee.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'myEmployees':myEmployees
    }
    return HttpResponse(template.render(context,request))

def create(request):
    template = loader.get_template('createPage.html')
    return HttpResponse(template.render({}, request))