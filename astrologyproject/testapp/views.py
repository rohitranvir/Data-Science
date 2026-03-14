from django.shortcuts import render
import datetime,random
# Create your views here.
def result_view(request):
    msg=[
        'The golden days is ahead',
        'Better to sleep More in classroom',
        'Towmarrow will be the Best days in your life',
        'Towmarrow is the perfect days to purpose to your girlfriend',
        'Very soon you will get a job',

    ]
    names_list=['katrina','karina','Madhuri','Deepika','Lilly']
    time=datetime.datetime.now()
    h=int(time.strftime('%H'))
    if h < 12:
        s = 'Good Morning'
    elif h < 16:
        s = 'Good Afternoon'
    elif h < 21:
        s = 'Good Evening'
    else:
        s = 'Good Night'
    name=random.choice(names_list)
    msg=random.choice(msg)
    my_dict={
        'time':time,'name':name,'msg':msg,'wish':s
    }
    return render(request,'testapp/results.html',my_dict)