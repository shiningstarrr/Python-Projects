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
- Bootstrap: https://getbootstrap.com/
- Python Shell Queries: https://docs.djangoproject.com/en/4.2/topics/db/queries/
- Complete Queryset API: https://docs.djangoproject.com/en/4.2/ref/models/querysets/#queryset-api
- Queryset limiting field reference: https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups
- 


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
- Create index.html under templates folder
- Add templates in view.py:
```ruby
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

```


# Bootstrap
- Copy Bootstrap template into index.html
- Create table in models.py
```ruby
class Employee(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
```
- Migrate the database: ```python manage.py makemigrations employee```, then ```python manage.py migrate```


# Add data into database/models.py
- in terminal: ```python manage.py shell```
    >>> from employee.models import Employee
    >>> emp = Employee(name='John',title='Manager')
    >>> emp.save()
    >>> Employee.objects.all().values()



# using model in index.html
- Pass Employee into index.html:
```ruby
def index(request):
    myEmployees = Employee.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'myEmployees':myEmployees
    }
    return HttpResponse(template.render(context,request))
```
- ```{% for x in myEmployees %}, {% endfor %}, {{x.name}}, {{x.title}}```


# Simple form page (CREATE)
- Create createPage.html and pass into urls.py: ```path('create/',views.create,name = 'create')```
- Add function in views.py:
```ruby
def create(request):
    template = loader.get_template('createPage.html')
    return HttpResponse(template.render({}, request))
```


# Send form data to database
```ruby
def createData(request):
    data1 = request.POST['name'],
    data2 = request.POST['title']
    newEmployee = Employee(name=data1,title=data2)
    newEmployee.save()
    return HttpResponseRedirect(reverse('index')) 
```
## Create link to direct to create page
```ruby
    <a href="http://127.0.0.1:8000/employee/create/">
    Create
    </a>     
```


# DELETE, UPDATE, RECAP







# Django extension in vscode and django tips
# Cleanup the code
# Create SUPERUSER
# Easy to use admin panel
# ADMIN. py
# model (database) for blog page
# Bootstrap for blog page
# Blog. html