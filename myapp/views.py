from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
import random
from myapp.models import student

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


# ========== student =================
# student index page
def student_index(request):
    return render(request, "student.html")

# student add page
def student_add(request):
    return render(request, "student_add.html")

# student save data to DB
def student_post(request):
    if request.method == "POST":
        cName = request.POST["cName"]
        cGender = request.POST["cGender"]
        cBirthday = request.POST["cBirthday"]
        cEmail = request.POST["cEmail"]
        cPhone = request.POST["cPhone"]
        cAddr = request.POST["cAddr"]

        data = student.objects.create(cName=cName, cGender=cGender, cBirthday=cBirthday, cEmail=cEmail, cPhone=cPhone, cAddr=cAddr)
        
        data.save()

        return redirect('/student')
    else:
        error_message = "請重新輸入資料"

    return render(request, "student_add.html", locals())


# ========== student =================