import random
import django
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sunnyjobs.settings')
django.setup()
from faker import Faker
from testapp.models import Bangjobs,Punejobs,HydJobs
f=Faker()

def phoneno():
    d1=str(random.randint(6,9))
    num=str(d1)
    for i in range(9):
        num+=str(random.randint(0,9))
    return int(num)
def title():
    l=["Web Developer","Python Developer","Data Analyst","Frontend Dev","Backend Dev"]
    return random.choice(l)
def eligibil():
    l=["12th Pass","Graduate","B.Tech","Any Degree"]
    return random.choice(l)
def populate(n,tab):
    for i in range(n):
        fdate=f.date()
        fcompany=f.company()[:30]
        ftitle=title()
        feligibility=eligibil()
        faddr=f.address()
        femail=f.email()
        fphone=phoneno()
        tab.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            eligibility=feligibility,
            address=faddr,
            email=femail,
            phonenumber=fphone
        )
tab_check={
    "pune":Punejobs,
    "bang":Bangjobs,
    "hyd":HydJobs
}
n=int(input("Enter value that you want to enter in database : "))
tab=input(("Enter a table Name You want to insert a data (pune,bang,hyd) : "))
if tab in tab_check:
    print("Inserting started ........")
    populate(n,tab_check[tab])
    print("Record inserted successfull ✅")
else:
    print("Table name Wrong")
