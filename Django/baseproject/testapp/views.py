from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_view(request):
    return HttpResponse('<h1>This is first view responsed </h1>')
def second_view(request):
    return HttpResponse('<h1>This is second view responsed </h1>')
def third_view(request):
    return HttpResponse('<h1>This is third view responsed </h1>')
