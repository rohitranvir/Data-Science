from django.db import models
class Person(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()

class Employee(Person):
    eno=models.IntegerField()
    esal=models.IntegerField()

class Manager(Employee):
    exp=models.IntegerField()
    team_size=models.IntegerField()

class ContactInfo1(models.Model):
    name = models.CharField(max_length=30, default='')
    email = models.EmailField(null=True)
    address = models.CharField(max_length=200, null=True)


class Students1(ContactInfo1):
    rollno = models.IntegerField()
    marks = models.IntegerField()


class Teacher1(ContactInfo1):
    subject = models.CharField(max_length=100)
    salary = models.IntegerField()


class ContactInfo(models.Model):
    name = models.CharField(max_length=30, default='')
    email = models.EmailField(null=True)
    address = models.CharField(max_length=200, null=True)
    class Meta:
        abstract = True


class Students(ContactInfo):
    rollno = models.IntegerField()
    marks = models.IntegerField()


class Teacher(ContactInfo):
    subject = models.CharField(max_length=100)
    salary = models.IntegerField()