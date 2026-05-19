from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
class EmployeeListAPIview(APIView):
    def get(self,request):
        qs=Employee.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        return Response(serializer.data)

