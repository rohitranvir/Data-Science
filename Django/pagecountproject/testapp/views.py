from django.shortcuts import render

# Create your views here.
def page_count_view(request):
    print("Cookies from the client ",request.COOKIES)
    count=(int(request.COOKIES.get('count',0)))
    count+=1
    response=render(request,'testapp/index.html',{"count":count})
    response.set_cookie('count',count)
    return response
