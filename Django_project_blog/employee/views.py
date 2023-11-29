import http
from json import load
from multiprocessing import context
from re import template
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import BlogPosts, Employee
from django.db.models import Q

# Create your views here.
def index(request):
    myEmployees = Employee.objects.all().values()
    template = loader.get_template('employee/index.html')
    context = {
        'myEmployees':myEmployees
    }
    return HttpResponse(template.render(context,request))

def create(request):
    template = loader.get_template('employee/createPage.html')
    return HttpResponse(template.render({}, request))

def createData(request):
    data1 = request.POST['name']
    data2 = request.POST['title']
    newEmployee = Employee(name=data1,title=data2)
    newEmployee.save()
    return HttpResponseRedirect(reverse('employee')) # The reverse() function can reverse a large variety of regular expression patterns for URLs

def delete(request,id):
    del_emp = Employee.objects.get(id=id)
    del_emp.delete()
    return HttpResponseRedirect(reverse('employee'))

def update(request,id):
    update_emp = Employee.objects.get(id = id)
    template = loader.get_template('employee/updatePage.html')
    context={
        'Employee':update_emp
    }
    return HttpResponse(template.render(context,request))

def updateData(request,id):
    data1 = request.POST['name']
    data2 = request.POST['title']
    update_emp = Employee.objects.get(id = id)
    update_emp.name = data1
    update_emp.title = data2
    update_emp.save()
    return HttpResponseRedirect(reverse('employee')) 

# For blog page:
def blog(request):
    posts = BlogPosts.objects.all()
    featuredPost = BlogPosts.objects.filter(featured = True)
    template = loader.get_template('employee/blog.html')
    context = {
        'posts':posts,
        'featuredPost':featuredPost,
    }
    return HttpResponse(template.render(context, request))