from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = "homePage"),
] 
# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)