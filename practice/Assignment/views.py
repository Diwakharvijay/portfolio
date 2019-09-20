from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.
def welcome(request):
    return render(request,'welcome.html',{'name':'CallHub'})

def add(request):
    start_time=time.time()
    val=int(request.POST['num'])
    a,b=1,1
    if val==1:
        print(a)
    else:
        for i in range(2,val):
            res = a+b
            a,b = b,res
            print(res)
    end_time=time.time()
    Time=str(round((end_time-start_time),3))+'secs'
    return render(request,'result.html',{'result':res,'time_cal':Time,'enter_num':val})