from django.shortcuts import render
from posts.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, permissions, generics
from .models import Post, Author
from .serializers import PostSerializer, AuthorSerializer
from django.http import HttpResponseRedirect

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = [IsOwnerOrReadOnly]

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer