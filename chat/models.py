from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    Username=models.CharField(max_length=150)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=200)
    email=models.EmailField()
    
