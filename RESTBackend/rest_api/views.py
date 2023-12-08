from telnetlib import STATUS
from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
@api_view(['GET', 'POST'])
def PostsView(request):
    if request.method == 'GET':
        posts = Post.objects.all() # querySet
        serializer = PostSerializer(posts, many=True) # many for fetching all data
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 201 -> created
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET', 'PUT','DELETE'])
def posts_detail(request, id):
    try:
        post = Post.objects.get(id = id)
    except Post.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':

        serializer = PostSerializer(post, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)