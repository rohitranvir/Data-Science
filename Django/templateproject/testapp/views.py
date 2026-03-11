from django.shortcuts import render
import datetime
# Create your views here
def wish(requests):
    date=datetime.datetime.now()
    msg="Hello end user Good"
    h=int(date.strftime('%H'))
    if h<12:
        msg+='Morning'
    elif h<16:
        msg+='Afternoon'
    elif h<21:
        msg+='Evining'
    else:
        msg+='Night'
    my_dict={'date':date,'msg':msg}
    return render(requests,'testapp/wish.html',my_dict)