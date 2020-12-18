from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField( verbose_name='email', max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    REQUIRED_FIELDS = ['username','first_name','last_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email