from django.shortcuts import render,redirect
from . import models
from .models import User,Request
import bcrypt

def home(request):
    return render(request,'login.html')

def student(request):
    thisUser = User.objects.get(id = request.session["id"])
    thisUserRequests = thisUser.request.all()
   
    context={
        "user":User.objects.get(id=request.session["id"]),
        "requests":thisUserRequests, 
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
                    request.session['id']=user[0].id
                else:
                    request.session['id']= User.objects.get(email=request.session["email"]).id
                    return redirect("/student_profile")              
    return redirect("/")

def request(request):
    if "email" not in request.session:
        return redirect("/")
    if request.method=="POST":
        user = models.User.objects.get(email =request.session['email'] )
        models.create_request(request.POST,user)
        return redirect("/student_profile")

def attendance(request):
    return render(request,"attendance.html")

def tickets(request):
    context={
        "requests":models.Request.objects.all()
    }
    return render(request,"tickets.html",context)

def logout(request):
    request.session.clear()
    return redirect('/')

# Create your views here.
