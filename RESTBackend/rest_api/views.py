from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.

def Posts(request):
    if request.method == 'GET':
        posts = Post.objects.all() # querySet
        serializer = PostSerializer(Post, many=True) # many for fetching all data
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201) # 201 -> created
        return JsonResponse(serializer.errors, status = 400)
