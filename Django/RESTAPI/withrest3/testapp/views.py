from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.generics import ListAPIView,RetrieveAPIView
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
class EmployeeListAPIview(APIView):
    def get(self,request):
        qs=Employee.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        return Response(serializer.data)

class EmployeeCreateModelMixins(mixins.CreateModelMixin,ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def  post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
class EmployeeRetriveDestroyModelMixins(mixins.UpdateModelMixin,mixins.DestroyModelMixin,RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def  put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def  delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    def  patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)