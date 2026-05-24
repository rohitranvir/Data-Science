from django.shortcuts import render
from testapp.models import Employee
from rest_framework import viewsets
from testapp.serializers import EmployeeSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
class EmployeeCBVView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]