from django.shortcuts import render

# Create your views here.
def result_view(request):
    subjects={
        's1':'python',
        's2':'Django',
        's3':'restapi',
        's4':'Numpy'
    }
    return render(request,'testapp/result.html',subjects)
