import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelproject3.settings')
django.setup()
from testapp.models import Student
from faker import Faker
from random import *
def phonenu():
    d1=randint(6,9)
    num=str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        f = Faker()
        frollno=f.random_int(min=1,max=999)
        fname=f.name()
        fdob=f.date()
        fmarks=f.random_int(min=20,max=99)
        femail=f.email()
        fphone=phonenu()
        Student.objects.get_or_create(
            rollno=frollno,
            name=fname,
            dob=fdob,
            marks=fmarks,
            email=femail,
            phonenumber=fphone
        )
n=int(input("Enter a value  to insert a record : "))
populate(n)
print("record inserted")