from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
# Create your views here.
class TESTViewSet(ViewSet):
    def list(self):
        color=['blue','red','green']
        return Response({'msg':'This is List ','color':color})
    def retrive(self,request,pk=None):
        return Response({'msg':'This is from Retrive '})
    def partial_update(self,request,pk=None):
        return Response({'msg':'This is from Retrive '})
    def update(self,request,pk=None):
        return Response({'msg':'This is from update '})
    def delete(self,request,pk=None):
        return Response({'msg':'This is from delete '})
class TestAPIView(APIView):
    def get(self,request,*args,**kwargs):
        colors=['red','blue','green']
        return Response({'msg':'Happy holi','color':colors})
    def put(self,request,*args,**kwargs):
        colors=['red','blue','green']
        return Response({'msg':'This message from Put','color':colors})
    def post(self,request,*args,**kwargs):
        colors=['red','blue','green']
        return Response({'msg':'This message from POST','color':colors})
    def patch(self,request,*args,**kwargs):
        colors=['red','blue','green']
        return Response({'msg':'This message from Patch','color':colors})