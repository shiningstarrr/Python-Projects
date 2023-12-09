from django.urls import include, path
from .views import PostViewSet, PostsView, posts_detail, PostsAPIView, postDetailsAPIView,genericApiView,genericViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register('posts', genericViewSet, basename='posts')

urlpatterns = [
    # path('posts/', PostsView),
    # path('details/<int:id>', posts_detail)

    # path('posts/', PostsAPIView.as_view()),
    # path('details/<int:id>', postDetailsAPIView.as_view()),

    path('postsid/<int:id>', genericApiView.as_view()),
    path('', include(router.urls)),
]
