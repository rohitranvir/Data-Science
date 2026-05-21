from django.shortcuts import render

# Create your views here.
from testapp.serializer import EmployeeSerializer
from testapp.models import Employee
from rest_framework import viewsets 
class EmployeeViewCrudCBV(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    