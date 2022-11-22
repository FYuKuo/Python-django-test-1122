from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random

# Create your views here.

def sayHi(request):
    return HttpResponse('<h1>Hi Django!</h1>')

def Hihi(request,name):
    return HttpResponse(f'<h1>Hi {name}!</h1>')

def hello(request,name):
    now = datetime.now()
    return render(request,"hello.html",locals())

def dice(request):
    no = random.randint(1,6)
    return render(request,"dice.html",{"no":no})

