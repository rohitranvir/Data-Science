from django.http import HttpResponse
class AppUnderMaintainnce(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        return HttpResponse('<h1>Currently app under maintainance</h1>')