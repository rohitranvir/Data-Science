from django.db import models

# Create your models here.
class StudentManager(models.Manager):
    def get_high_sal(self):
        return self.filter(marks__gte=75)
class Student(models.Model):
    name=models.CharField(max_length=30)
    marks=models.IntegerField()
    objects = StudentManager()