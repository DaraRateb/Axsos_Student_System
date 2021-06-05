from django.db import models

class Role(models.Model):
    name=models.CharField(max_length=225)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=15)
    image=models.ImageField(upload_to="img/%y",null=True)
    email=models.EmailField(max_length=225)
    password=models.CharField(max_length=225)
    # role_user = models.ForeignKey(Role, related_name="user", on_delete = models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    
# Create your models here.
def get_user(info):
    return User.objects.filter(email=info["email"])

