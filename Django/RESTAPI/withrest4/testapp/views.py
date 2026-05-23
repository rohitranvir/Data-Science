from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from testapp.serializer import EmployeeSerializer
from testapp.models import Employee
from rest_framework import viewsets 
class EmployeeViewCrudCBV(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    permission_classes=[IsAdminUser]
    authentication_classes=[TokenAuthentication]
    