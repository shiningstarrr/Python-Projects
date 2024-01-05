from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/', views.todos, name='detail'),
    path('addTask/', views.addTask, name='addTask'),
    path('markDone/<int:id>', views.markDone, name='markDone'),
    path('remove/<int:id>', views.remove, name='remove'),
    path('editTask/<int:id>', views.edit_task, name='editTask'),
] 