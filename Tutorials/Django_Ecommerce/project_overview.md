# Seting up
- Create Virtual Env: ```py -3 -m venv .venv```
- Add git ignore: .gitignore file
- Install Django: ```python -m pip install Django```
- Update pip: ```python.exe -m pip install --upgrade pip```
- Install django rest framework: ```python -m pip install djangorestframework```
- Install pillow: ```pip install pillow```
- Create project: ```django-admin startproject mysite .```
- Start app: ```django-admin startapp ecommerce```
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
STATIC_TOOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    'mysite/static'
]
```
