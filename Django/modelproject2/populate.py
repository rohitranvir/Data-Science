import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelproject2.settings')
django.setup()
from faker import Faker
from testapp.models import temp
f=Faker()
from random import *
def phoneno():
    d1=str(randint(6,9))
    num=str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        feno=f.random_int(1,999)
        fename=f.name()
        fesal=f.random_int(1000,10000)
        faddr=f.address()
        temp.objects.get_or_create(
            eno=feno,
            ename=fename,
            esal=fesal,
            eaddr=faddr
        )
n=int(input("Enter value that you want to enter in database"))
populate(n)
print("Record inserted successfull")
