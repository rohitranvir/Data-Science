import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ormproject.settings')
import django
django.setup()
from testapp.models  import Employee
from faker import Faker
from random import *
faker=Faker()
def populate(n):
    for i in range(n):
        feno=randint(1000,9999)
        fname=faker.name()
        fesal=randint(10000,99999)
        faddr=faker.city
        emp_record=Employee.objects.get_or_create(
            eno=feno,
            ename=fname,
            esal=fesal,
            eaddr=faddr

        )
n=int(input("Enter a Number for data" ))
populate(n)
print("Data entered Successfully !")