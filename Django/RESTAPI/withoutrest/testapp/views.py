from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
import json
# Create your views here.
from django.views.generic import View
class jsonCBV(View):
    def get(self,request,*args,**kwargs):
        json_data={
            'msg':'this is from get'
        }
        return HttpResponse(json.dumps(json_data),content_type='application/json')
    def post(self,request,*args,**kwargs):
        json_data={
            'msg': 'this is from post'
        }
        return HttpResponse(json.dumps(json_data),content_type='application/json')
    def put(self,request,*args,**kwargs):
        json_data={
            'msg': 'this is from put'
        }
        return HttpResponse(json.dumps(json_data),content_type='application/json')
    def delete(self,request,*args,**kwargs):
        json_data={
            'msg': 'this is from delete'
        }
        return HttpResponse(json.dumps(json_data),content_type='application/json')

def emp_data_json_view(request):
    emp_Data={
        'eno':102,
        'ename':'Rohit',
        'esal':35000,
        'eaddr':'At post kali '
    }
    json_Data=json.dumps(emp_Data)
    return HttpResponse(json_Data,content_type='application/json')