from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sayHi(request):
    return HttpResponse('<h1>Hi Django!</h1>')
