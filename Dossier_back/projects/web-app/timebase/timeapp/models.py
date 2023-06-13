from django.db import models

class Users(models.Model):
    surname=models.fields.CharField(max_length=100)


# Create your models here.
