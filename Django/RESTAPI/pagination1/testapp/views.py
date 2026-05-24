from django.shortcuts import render
from rest_framework.generics import ListAPIView
from testapp.serializers import EmployeeSerializer
from testapp.models import Employee
from rest_framework.pagination import PageNumberPagination, CursorPagination
# Create your views here.
class MyPagination(PageNumberPagination):
    page_size = 6
    page_query_param = 'mypage'
class MyPagination2(CursorPagination):
    ordering = '-esal'
    page_size = 5
class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    search_fields = ("ename",)
