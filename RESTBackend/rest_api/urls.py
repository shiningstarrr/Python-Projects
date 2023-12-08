from django.urls import path
from .views import PostsView, posts_detail

urlpatterns = [
    path('posts/', PostsView),
    path('details/<int:id>', posts_detail)
]
