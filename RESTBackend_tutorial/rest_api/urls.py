from django.urls import path
from .views import PostsView, posts_detail, PostsAPIView, postDetailsAPIView,genericApiView

urlpatterns = [
    # path('posts/', PostsView),
    # path('details/<int:id>', posts_detail)

    # path('posts/', PostsAPIView.as_view()),
    # path('details/<int:id>', postDetailsAPIView.as_view()),

    path('posts/<int:id>', genericApiView.as_view()),
]
