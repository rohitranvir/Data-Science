from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def exams_view(request):
    return HttpResponse('<h1>Exam View</h1>')
def attedence_view(request):
    return HttpResponse('<h1>Attedence view</h1>')
def fees_view(request):
    return HttpResponse('<h1> Fees view</h1>')