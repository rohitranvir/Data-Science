from django.shortcuts import render, redirect
from testapp.models import Movie
from testapp.forms import Moviesform
# Create your views here.
def index_view(request):
    return render(request,'testapp/index.html')
def list_movies(request):
    movieslist=Movie.objects.all()
    return render(request,'testapp/list_movies.html',{'movieslist':movieslist})
def add_movie(request):

    if request.method=="POST":
        form=Moviesform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(index_view)
    form = Moviesform()
    return render(request,'testapp/add_movie.html',{'form':form})