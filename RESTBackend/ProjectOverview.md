# Django Rest Framework Project - Introduction
- Video Link: https://www.youtube.com/watch?v=z6WudaByH1k&t=5130s
- REST stands for Representational State Transfer Application Programming Interface
- Create Virtual Env: ```py -3 -m venv .venv```
- Add git ignore: .gitignore file
- Install Django: ```python -m pip install Django```
- Update pip: ```python.exe -m pip install --upgrade pip```
- Create project: ```django-admin startproject drf .```
- Start app: ```django-admin startapp rest_api```
- Install django rest framework: ```python -m pip install djangorestframework```

# Resources
- Django REST Framework: https://www.django-rest-framework.org/

# Start Project:
- Go to settings.py: add ```'rest_api','rest_framework',``` app to INSTALLED_APPS

# Serialization
- QuerySet: A collection of objects from your database
- Model Instances: An instance of the class represents one object from that model (which maps to one row of the table in the database)
- Serialization: QuerySet, Model instances -> convert to Native Python Datatype -> convert to JSON, XML, or other content Type

# Create the model
- Create Post model in models.py with title, author, and email
- Make migration: ```python manage.py makemigrations``` and ```python manage.py migrate```
- Create superuser: ```python manage.py createsuperuser```

# Register the model
- ```admin.site.register(Post)```

# Import Serializers
- In app folder (rest_api) create serializers.py file
- Create class PostSerializer
```ruby
class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(default = '')
    def create(self, validate_data):
        return Post.objects.create(validate_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', validated_data.title)
        instance.author = validated_data.get('author', validated_data.author)
        instance.email = validated_data.get('email', validated_data.email)
```
- In termail: 
>>> python manage.py shell
>>> from rest_api.models import Post
>>> from rest_api.serializers import PostSerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser
>>> post = Post(title = 'test title 1', author = 'star', email='email@example.com')
>>> post.save()
>>> serializer = PostSerializer(post)
>>> serializer.data
>>> content = JSONRenderer().render(serializer.data)
>>> content
>>> serializer = PostSerializer(Post.objects.all(), many = True)

# Model Serializer
- Recreate class PostSerializer, delete the previous one
```ruby
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        field = ['title', 'email', 'author']
```
- In terminal:
>>> serializer = PostSerializer()
>>> print(repr(serializer))

# Create a Normal Django Function Based Api View
- Import PostSerializer and Post into view.py
- Create Posts function with request method of 'GET' and 'POST'
- Create urls.py in app folder and add urlpatterns ```urlpatterns = [path('posts/', PostsView)]```
- Add path in project urls: ```path('', include('rest_api.urls')),```

# Http Methods:
- add ```@csrf_exempt```to views.py to get authenticated
- Create function posts_detail()

# Api View Decorator
- change ```@csrf_exempt``` to ```@api_view(['GET', 'POST'])```
- Reshape function PostViews and posts_detail

# Class-Based Api View
- We can write API views using class-based views, rather than function based views
- Create function PostsAPIView(APIView) and postDetailsAPIView(APIView) in views.py
- change url path in urls.py
```ruby
    path('posts/', PostsAPIView.as_view()),
    path('details/<int:id>', postDetailsAPIView.as_view()),
```

# Using mixins and generic class-based views
- Create function genericApiView with mixins methods in parameter
- 1.57