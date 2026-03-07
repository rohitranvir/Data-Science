from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.
def date_time_info(resuest):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    msg="<h1>Hello very good "
    if h<12:
        msg+="Good morning"
    elif h<16:
        msg+='Good Afternoon'
    elif h<21:
        msg+='Good evining'
    else:
        msg+="Good Night"
    msg+="</h1><hr>"
    return HttpResponse(msg+str(date))

