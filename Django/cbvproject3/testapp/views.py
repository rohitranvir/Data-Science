from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView,View


# Create your views here.
class TemplateCBV(TemplateView):
    template_name = 'testapp/result.html'

class HelloWorldView(View):
    def get(self,request):
        return HttpResponse('<h1>This is from classbased views</h1>')
class TemplateCBV2(TemplateView):
    template_name = 'testapp/result2.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='Sunny'
        context['marks']=99
        context['subject']='Python'
        return context