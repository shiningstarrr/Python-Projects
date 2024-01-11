from django.urls import path,include
from . import views

urlpatterns = [
    # Log-in Page
    path('', views.login, name="login"),
    # Home Page
    path('/appList', views.appList, name="appList"),
    # Todo App
    path('todoApp/', views.list_todos, name="list_todos"),
    # Blog Website
]