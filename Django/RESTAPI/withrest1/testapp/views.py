import requests.compat
from django.shortcuts import render

# Create your views here.
import io
from django.views.generic import View

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from testapp.serializers import EmployeeSerializer
from testapp.models import Employee
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt, name='dispatch')
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
    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        serializer=EmployeeSerializer(data=pdata)
        if serializer.is_valid():
            serializer.save()
            msg={
                'msg':'Record created successfull.......'
            }
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    def put(self,request,*args,**kwargs):
        json_Data=request.body
        stream=io.BytesIO(json_Data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id')
        emp=Employee.objects.get(id=id)
        serilizer=EmployeeSerializer(emp,pdata)
        if serilizer.is_valid():
            serilizer.save()
            msg={
                'msg':'Record inserted successfully.......'
            }
            json_Data=JSONRenderer().render(msg)
            return HttpResponse(json_Data,content_type='application/json')
        json_Data = JSONRenderer().render(serilizer.errors)
        return HttpResponse(json_Data, content_type='application/json')