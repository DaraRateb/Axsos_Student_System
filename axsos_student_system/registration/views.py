from django.shortcuts import render,redirect
from . import models
from .models import User
import bcrypt

def home(request):
    return render(request,'login.html')

def student(request):
    context={
        "user":User.objects.get(email=request.session["email"]), 
    }
    return render(request,"student_profile.html",context)

def instructor(request):

    context={
        "instructor":{"full_name":"Ibtisal Awashrah","phone_number":9088738973,"email":"ibtisal@axsos.me"}
    }
    return render(request,"instructor_profile.html",context)
    

def login(request):
    if request.method=="POST":
        user=models.get_user(request.POST)
        if user:
            if(request.POST['password'])==user[0].password:
            # if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()):
                if 'email' not in request.session:
                    request.session['email']=user[0].email
                if request.POST["email"] == "ibtisal@axsos.me":
                    return render(request,"instructor_profile.html")
                else:
                    context={
                                "user":User.objects.get(email=request.session["email"]), 
                            }
                    return render(request,"student_profile.html",context)


                
    return redirect("/")

def request(request):
    if "email" not in request.session:
        return redirect("/")
    if request.method=="POST":
        user = models.User.objects.get(email =request.session['email'] )
        models.create_request(request.POST,user)
        return redirect("/student_profile")

def logout(request):
    request.session.clear()
    print("lala**************")
    return redirect('/')

# Create your views here.
