from django.shortcuts import render
from typing_extensions import type_repr


# Create your views here.
def news_info(request):
    return render(request,'testapp/home.html')
def movie_view(request):
    head_msg="Movies information"
    msg1="Jailer was supper movie"
    msg2="DHURANDAR IS normal movie"
    msg3="Section 375 is good movie"
    type="movie"
    my_dict={"head_msg":head_msg,"msg1":msg1,"msg2":msg2,"msg3":msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)
def politics_info(request):
    head_msg="This is news Page"
    msg1="Corruption and misuse of power by politicians."
    msg2 = "Creates division and conflict among people."
    msg3 = "Decision-making is often slow due to bureaucracy and political interests."
    type = "politics"
    my_dict={"head_msg":head_msg,"msg1":msg1,"msg2":msg2,"msg3":msg3,'type':type}

    return render(request,'testapp/news.html',my_dict)
def sport_info(request):
    head_msg="This is sport page"
    msg1="Improves physical health and fitness."
    msg2="Builds teamwork, discipline, and leadership skills."
    msg3="Helps reduce stress and improves mental well-being. ⚽🏏💪"
    type = "sport"
    my_dict={"head_msg":head_msg,"msg1":msg1,"msg2":msg2,"msg3":msg3,'type':type}

    return render(request,'testapp/news.html',my_dict)