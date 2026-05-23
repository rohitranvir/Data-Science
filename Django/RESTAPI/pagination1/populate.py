import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pagination1.settings')
import django
django.setup()
from testapp.models import Employee
from faker import Faker
import random
faker = Faker()
def populate(n):
    for i in range(n):
        feno=random.randint(1000,9999)
        fename=faker.name()
        fesal=random.randint(1000,9999)
        faddr=faker.city()
        emp_records=Employee.objects.get_or_create(
            eno=feno,
            esal=fesal,
           ename=fename,
           addr=faddr
        )
n=int(input('Enter Number Of records'))
populate(n)
print(f'{n} of records populated.......')
