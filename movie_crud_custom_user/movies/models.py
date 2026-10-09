from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Movie(models.Model):
    title=models.CharField(max_length=100)
    director=models.CharField(max_length=100)
    language=models.CharField(max_length=50)
    year=models.IntegerField()
    rating=models.FloatField()
    runtime=models.IntegerField()
    image=models.ImageField(upload_to='movies',null=True)

class CustomUser(AbstractUser):
    phone=models.CharField(max_length=50,null=True)
    address=models.CharField(max_length=100,null=True)

