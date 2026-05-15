from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view_page(request):
    print(10/0)
    return HttpResponse('<h1>This is view function</h1>')