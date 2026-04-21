from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=250)
    auther=models.CharField(max_length=250)
    pages=models.IntegerField()
    price=models.IntegerField()