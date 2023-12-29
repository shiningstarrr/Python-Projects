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
- Django static files include css, image or javascript, we can create a folder named static to store those static files. 
- In settings.py: 
```ruby
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    'mysite/static'
]
```
- Then inside html file add on the top ```{% load static %}```
- For css style: ```<link rel="stylesheet" href = "{% static 'css/css_name' %}">```
- For image: ```<img src = "{% static 'images/image_name' %}" alt = "" width = "">```


# Django media files
- In root folder create a folder named media
- In settings.py: 
```ruby
# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```
- In urls.py:
```ruby
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
```

# Bring data to frontend
- Example in views.py:
```ruby
def home(request):
    employees = Employee.objects.all()
    context = {
        'employees':employees,
    }
    return render(request,'home.html',context)
```
- Example in home.html:
```ruby
{% for e in employees %}
{{e.id}} # Django will automatically generate primary key. Object's id will not change after deleting
{{forloop.counter}} # primary key that will change after deleting one object
<img class = "card-img-top" src = "{{e.photo}}" alt = "Employee Photo"> # add images
{% endfor %}
```

# Create urls for app
- views.py should either render http response or a html web page
- In project urls.py ```path('employees/', include('employees.urls', name = "..."))```
- Create urls.py in app folder
```ruby
from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>', views.employee_detail,name = ""),
]
```

# Link url to button or text
- In project urls.py, set name to urlpatterns. Ex: ```path('', views.home, name = 'url_name'),```
- In html file: ```<a href = "{% url 'url_name' %}", class = "btn btn-primary"> Back to home </a>```
- For url that takes id: ```<a href = "{% url 'url_name' employee.id %}"> {{emp.name}} </a>```