from django.shortcuts import render
from optree.functools import partial

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.response import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer,ProfileSerializer
class RegisterView(APIView):
    permission_classes=[AllowAny]
    def post(selfself,request):
        s=RegisterSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response({'message':'Registered Successfully'},status=201)
        return Response(s.errors,status=400)
class ProfileView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        return Response(ProfileSerializer(request.user).data)
    def patch(self,request):
        s=ProfileSerializer(request.user,data=request.data,partial=True)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors,status=400)

