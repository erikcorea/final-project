from django.db import models
from blog_users.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
