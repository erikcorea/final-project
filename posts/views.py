from django.shortcuts import render
from posts.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, permissions, generics
from .models import Post, Author
from .serializers import PostSerializer, AuthorSerializer
from django.http import HttpResponseRedirect

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        elif self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == 'update' or self.action == 'destroy' or self.action == 'partial_update':
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer