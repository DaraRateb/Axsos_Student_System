from django.shortcuts import render,redirect
from . import models
import bcrypt

def home(request):
    return render(request,'login.html')

def student(request):
    # if "first_name" in request.session:
        return render(request,"attendance.html")
    # return redirect("/")

def login(request):
    if request.method=="POST":
            # if request.POST:
                # user=models.get_user(request.POST)
                # if user.role=="":
                #     if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()):
                #         if 'first_name' not in request.session:
                #             request.session['first_name']=user[0].first_name
        return redirect("/student_profile")
    else:
        return redirect('/')


# Create your views here.
