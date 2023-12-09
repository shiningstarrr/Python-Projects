from telnetlib import STATUS
from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


# Generic ViewSetss
class genericViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


# Viewsets
class PostViewSet(viewsets.ViewSet):
    def list(self, request):
        posts = Post.objects.all() 
        serializer = PostSerializer(posts, many=True) 
        return Response(serializer.data)
    def create(self, request):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



# Generic Classed-based views
class genericApiView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin, mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,id):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def post(self, request):
        return self.create(request)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        return self.destroy(request,id)

    

# Classed-based views
class PostsAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all() 
        serializer = PostSerializer(posts, many=True) 
        return Response(serializer.data)
    def post(self, request):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class postDetailsAPIView(APIView):
    def get_object(self, id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            raise Http404
        
    def get(self, request, id):
        post = self.get_object(id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, id):
        post = self.get_object(id)
        serializer = PostSerializer(post, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,id):
        post = self.get_object(id)
        post.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


# API View Decorator
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