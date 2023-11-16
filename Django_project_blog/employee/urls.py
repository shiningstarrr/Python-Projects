from venv import create
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('create/',views.create,name = 'create'),
    path('create/createData/',views.createData,name = 'createData')
]
