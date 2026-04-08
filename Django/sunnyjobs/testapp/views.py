from django.shortcuts import render

# Create your views here.
def home_page_views(request):
    return render(request,'testapp/home.html')

from testapp.models import HydJobs,Bangjobs,Punejobs

def hyd_jobs_view(request):
    jobs_list=HydJobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',my_dict)

def bang_jobs_view(request):
    jobs_list=Bangjobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/bangjobs.html',my_dict)

def pune_jobs_view(request):
    jobs_list=Punejobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/punejobs.html',my_dict)
