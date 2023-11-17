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
- Insertion:
    >>> from employee.models import Employee
    >>> emp = Employee(name='John',title='Manager')
    >>> emp.save()
- Update:
    >>> emp = Employee.objects.get(id=1)
    >>> emp.name = 'newName'
    >>> emp.save()
- Retrieve:
    + Retrieve specific objects:
    >>> Employee.objects.all()
    >>> Employee.objects.all().values()
    >>> Employee.objects.all().filter(name='rose')
    + Chaining filter:
    >>> Employee.objects.all().exclude(...).filter(...)
    >>> q = Employee.objects.filter(id=1), print(q.values())
    + Filtered querysets are unique:
    >>> q1 = Employee.objects.filter(...)
    >>> q2 = q1.exclude(pub_date__gte=datetime.date.today())
    >>> q3 = q1.filter(pub_date__gte=datetime.date.today())
    + Retrieve a single object:
    >>> Employee.objects.get(...)
- Limiting QuerySets:
    >>> Employee.objects.all()[:5]
    >>> Employee.objects.all()[:10:2]
    >>> Employee.objects.order_by("headline")[0] 
    which equals to:
    >>> Entry.objects.order_by("headline")[0:1].get()
    + A case-insensitive match, same as 'iexact':
    >>> Blog.objects.get(name__iexact="beatles blog")
    + same as 'exact':
    >>> Entry.objects.get(headline__exact="Cat bites dog")
    + A case-insensitive match, same as 'contains' or 'like':
    >>> Entry.objects.get(headline__icontains="Lennon")
    >>> Employee.objects.filter(name__contains='R').values()
    + same as 'in':
    >>> Entry.objects.filter(id__in=[1, 3, 4])
    + 'gt' greater than, 'gte' greater than or equal to, 'it' less than, 'ite' less than or equal to:
    >>> Entry.objects.filter(id__gt=4)
    + 'startswith' and 'endswith' case-sensitive, 'istartswith' and 'iendswith' case-insensitive:
    >>> Entry.objects.filter(headline__startswith="Lennon")
- Compare between fields:
    >>> from django.db.models import F
    >>> Employee.objects.filter(name=F('title')).values()



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




# DELETE, UPDATE, RECAP
# Django extension in vscode and django tips
# Cleanup the code
# Create SUPERUSER
# Easy to use admin panel
# ADMIN. py
# model (database) for blog page
# Bootstrap for blog page
# Blog. html