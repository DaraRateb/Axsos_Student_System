from django.shortcuts import render,redirect
# from .form import ImageForm
# from .models import Image


# def index(request):
#     if request.method == "POST":
#         form=ImageForm(data=request.POST,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             obj=form.instance
#             request.session['img']=obj.image.url               
            
#             return render(request,"index.html",{"obj":obj})

#     else:
#         form=ImageForm()
#     img=Image.objects.all()
    
    
#     return render(request,"login.html",{"img":img,"form":form})

def index(request):
    return render(request,'login.html')