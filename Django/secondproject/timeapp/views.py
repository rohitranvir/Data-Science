from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime
def times(request):
    date=datetime.datetime.now()
    s="<h1>Hello good Morning!!! </h1>"
    s1='<h2> Current time is '+str(date)+'</h2>'
    return HttpResponse(s+s1)