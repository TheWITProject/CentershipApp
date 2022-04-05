from operator import mod
from django.db import models
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=80)
    username = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    password1 = models.CharField(max_length=80)
    password2 = models.CharField(max_length=80)

