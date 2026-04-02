from django.shortcuts import render

# Create your views here.
def base_view(request):
    return render(request,'testapp/base.html')

def movie_view(request):
    return render(request,'testapp/Movie.html')
def sport_view(request):
    return render(request,'testapp/sport.html')
def politics_view(request):
    return render(request,'testapp/politics.html')