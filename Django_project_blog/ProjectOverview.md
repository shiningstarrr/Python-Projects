- Django Templates
- Django Admin
- CRUD 
- Variables, Tags, Statements, Loop, QuerySets

# Setting up
- Create Virtual Environment: ```py -3 -m venv .venv```
- Install Django: ```python -m pip install Django```
- Update pip version: ```python.exe -m pip install --upgrade pip```
- Check Django version: ```django-admin --version```
- Django all commands: ```django-admin```


# Start project
- Use command ```django-admin startproject learningDjango```
- Run server: ```python manage.py runserver port_number```
- Start project: ```django-admin startapp app_name```
- Migrate: ```python manage.py migrate```


# Resources:
- Resolve Django import: https://www.youtube.com/watch?v=QF0UJeKCM-8


# Create Super User
- ```python manage.py createsuperuser```


# Creating URLS
## In APP
- Create Http Response in view.py: 
```ruby
    def index(request):
        return HttpResponse('<h1>Hello from Employee</h1>')
```
- Create urls.py file in app, call function in views.py:
```ruby
    urlpatterns = [
        path('', views.index,name = 'index') # Inside '', put name of the url
    ]
```
## In Project
- Add app_name in project -> settings.py -> ```INSTALLED_APPS```
- Register URl in main project in file project -> urls.py:
```ruby
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('employee/',include('employee.urls'))
    ]
```


# Index.html




# Bootstrap
# Index.html continue
# models.py(database)