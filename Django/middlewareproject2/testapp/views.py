from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home_page_view(request):
    return HttpResponse('<h1>Hello this response from view</h1>')