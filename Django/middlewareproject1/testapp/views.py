from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome_view(request):
    print('This is by Views............')
    return HttpResponse('<h1>Middleware Successfull....</h1>')