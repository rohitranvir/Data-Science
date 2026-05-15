from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    print('printed by View function')
    return HttpResponse('<h1>THis is from View</h1>')