from rest_framework import serializers
from .models import Author, Post
class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(
        source='author.username',
        read_only=True
    )
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'author')
class AuthorSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ('id', 'name', 'nationality', 'posts')