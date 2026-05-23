from django.shortcuts import render
from rest_framework.generics import ListAPIView
from testapp.serializers import EmployeeSerializer
from testapp.models import Employee
# Create your views here.
class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer