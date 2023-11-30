from venv import create
from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog,name = 'blog'),

    path('employee/',views.index,name = 'employee'),
    path('create/',views.create,name = 'create'),
    path('create/createData/',views.createData,name = 'createData'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('update/<int:id>',views.update,name = 'update'),
    path('update/updateData/<int:id>', views.updateData,name='updateData'),
    path('details/<int:id>', views.detailsPage, name = 'details'),

]
