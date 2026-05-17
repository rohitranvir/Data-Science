from django.shortcuts import render

# Create your views here.
import io
from django.views.generic import View

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from testapp.serializers import EmployeeSerializer
from testapp.models import Employee
from django.http import HttpResponse



class EmployeeCBV(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id',None)
        if id is not None:
            emp=Employee.objects.get(id=id)
            serializer=EmployeeSerializer(emp)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        emp=Employee.objects.all()
        serializer=EmployeeSerializer(emp)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')