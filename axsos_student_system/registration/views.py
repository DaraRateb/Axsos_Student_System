from django.shortcuts import render,redirect
from . import models
from .models import User
import bcrypt

def home(request):
    return render(request,'login.html')

def student(request):
    if "email" in request.session:
        if request.session['email']=="ibtisal@axsos.me":
            return render(request,"instructor_profile.html")
        else:
            return render(request,"student_profile.html")
    return redirect("/")

def login(request):
    if request.method=="POST":
        user=models.get_user(request.POST)
        if user:
            if(request.POST['password'])==user[0].password:
            # if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()):
                if 'email' not in request.session:
                    request.session['email']=user[0].email
                return redirect('/student_profile')
            else:
                return redirect("/")
        else:
                return redirect("/")


# Create your views here.
