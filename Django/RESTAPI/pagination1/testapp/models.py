from django.db import models

# Create your models here.
class Employee(models.Model):
    eno= models.CharField(max_length = 100)
    ename = models.CharField(max_length = 100)
    esal = models.FloatField()
    addr=models.CharField(max_length = 100)