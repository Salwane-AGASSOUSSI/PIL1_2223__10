from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    num_id = models.IntegerField()



class Account_Request(models.Model):
    username = models.CharField(max_length=63)
    email = models.CharField(max_length=63)
    num_id = models.IntegerField()
    password = models.CharField(max_length=63,default='my password')
    is_approved = models.BooleanField(default=False)
    
    