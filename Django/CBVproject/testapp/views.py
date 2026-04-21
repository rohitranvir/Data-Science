from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Templatecbv(TemplateView):
    template_name = 'testapp/result.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='rohit'
        context['marks']=95
        context['subject']='Python'
        return context