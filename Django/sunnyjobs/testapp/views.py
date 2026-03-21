from django.shortcuts import render

# Create your views here.
def home_page_views(request):
    return rander(request,'testapp/index.html')