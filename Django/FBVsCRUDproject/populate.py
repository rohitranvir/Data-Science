import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FBVsCRUDproject.settings')
import django
django.setup()
from faker import Faker
faker=Faker()
from random import *
from testapp.models import Employee
def populate(n):
    for i in range(n):
        fname=faker.name()
        fsal=randint(10001,90009)
        feno=randint(101,999)
        faddr=faker.address()
        employee_record=Employee.objects.get_or_create(
            eno=feno,
            ename=fname,
            esal=fsal,
            addrs=faddr
        )
populate(5)
print("Record Inserted successfully")