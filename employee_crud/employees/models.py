from django.db import models

# Create your models here.

class Employee(models.Model):
    empid=models.IntegerField(unique=True)
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    place=models.CharField(max_length=30)
    gender_choices=[('male','Male'),('female','Female')]    # ('db value','display value)
    gender=models.CharField(max_length=20,choices=gender_choices)
    joiningdate=models.DateField()
    salary=models.IntegerField()
    designation=models.CharField(max_length=30)
    profile=models.ImageField(upload_to='profiles',null=True)