# Seting up
- Create Virtual Env: ```py -3 -m venv .venv```
- Add git ignore: .gitignore file
- Install Django: ```python -m pip install Django```
- Update pip: ```python.exe -m pip install --upgrade pip```
- Install django rest framework: ```python -m pip install djangorestframework```
- Install pillow: ```pip install pillow```
- Create project: ```django-admin startproject mysite .```
- Start app: ```django-admin startapp ecommerce```
- Basic commands: ```python manage.py makemigrations employee```, ```python manage.py migrate```, ```python manage.py createsuperuser```
- Add app into INSTALLED_APPS in manage.py
- Django MVT model:
User <-> Django <-> URL <-> Views <-> Model <-> Database
                              \         /
                               Template


# Django static files
- Django static files include css, image or javascript, we can create a folder named static to store those static files. From https://docs.djangoproject.com/en/4.0/howto/static-files/
- Typical development congig:
```ruby
# settings.py
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static',]
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
```
- Then inside html file add on the top ```{% load static %}```
- For css style: ```<link rel="stylesheet" href = "{% static 'css/css_name' %}">```
- For image: ```<img src = "{% static 'images/image_name' %}" alt = "" width = "">```


# Django media files
- media files are user-generated content like uploaded images or videos. From https://testdriven.io/blog/django-static-files/
- In root folder create a folder named media
- Typical development config: 
```ruby
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'uploads'

# urls.py
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
```

# Model file
- Create model class: ```class Weapons(models.Model):```
- Model Field
    + models.CharField(max_length=)
    + models.ImageField(upload_to='')
    + models.EmailField(max_length= , unique=True)
    + models.DateTimeField(auto_now_add=True)
    + models.DateTimeField(auto_now=True)
- Register models in admin
```ruby
# admin.py
from .models import Employee
admin.site.register(Employee)
```

# Bring data to frontend
- Create function for rendering page from templates/home.html Example
```ruby
# views.py
def home(request):
    employees = Employee.objects.all()
    context = {
        'employees':employees,
    }
    return render(request,'home.html',context)
```
- Import data into html page Example
```ruby
# home.html
{% for e in employees %}
{{e.id}} # Django will automatically generate primary key. Object's id will not change after deleting
{{forloop.counter}} # primary key that will change after deleting one object
<img class = "card-img-top" src = "{{e.photo.url}}" alt = "Employee Photo"> # add images
{% endfor %}
```

# Create urls for app
- views.py should either render http response or a html web page
- urls created for project and app
```ruby
# project: 
path('', include('employees.urls')), # app name+ urls
# app:
from django.urls import path
from . import views
path('home/', views.home, name='home'),
path('<int:pk>', views.employee_detail, name = ""),
```

# Link url to button or text
- In project urls.py, set name to urlpatterns. Ex: ```path('', views.home, name = 'url_name'),```
- In html file: ```<a href = "{% url 'url_name' %}", class = "btn btn-primary"> Back to home </a>```
- For url that takes id: ```<a href = "{% url 'url_name' employee.id %}"> {{emp.name}} </a>```

# Admin Panel
- List model fields in admin panel page, Ex: 
```ruby
# admin.py
class TaskAdmin(admin.ModelAdmin):
    list_display=('task', 'is_completed','updated_at') # Model fields you want to show 
    search_fields = ('task',) # fields you want to search in the search bar
admin.site.register(Task, TaskAdmin) # register model and class name
```

# CSRF Token (cross-site request forgery)
- When loading form with POST method, use csrf_token:
```ruby
# detail.html
<form action="{% url 'addTask' %}" method="POST"> # url + url name in url patterns
{%csrf_token%} 
<button type="submit" ... >submit</button>
</form>
```

# Get posted data from frontend
- request.POST
```ruby
# html page
<form action="{% url 'addTask' %}" method="POST"> 
<input type="text" name="task" class="form-control" placeholder="Add a task">
...
# views.py
task = request.POST['task'] # 'task' is the name attribute of the input field
Task.objects.create(task=task, is_completed=False) # create instance in Task model
return redirect('detail') # redirect to another page, name from urls.py
```

# CRUD & Primary Key
```ruby
# urls.py
path('markDone/<int:id>', views.markDone, name='markDone')
# views.py
def markDone(request,id):
# html page
<a href="{% url 'markDone' t.id %}" ... > </a>
```

