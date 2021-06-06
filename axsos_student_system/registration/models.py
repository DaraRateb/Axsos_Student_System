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

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class WorkingDays(models.Model):
    date=models.DateField()
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

class Attendance(models.Model):
    attended=models.BooleanField()
    user_attendance = models.ForeignKey(User, related_name="attendance", on_delete = models.CASCADE)
    workingdays_attendance = models.ForeignKey(WorkingDays, related_name="work_day", on_delete = models.CASCADE, null=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

class RequestStatus(models.Model):
    status=models.CharField(max_length=225)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

class Request(models.Model):
    description=models.TextField(max_length=500)
    date=models.DateField()
    user_request = models.ForeignKey(User, related_name="request", on_delete = models.CASCADE)
    requeststatus_request = models.ForeignKey(RequestStatus, related_name="status_foreign", on_delete = models.CASCADE, null=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    
# Create your models here.
def get_user(info):
    return User.objects.filter(email=info["email"])

def create_request(info,user):
    Request.objects.create(date=info["date"],description=info["description"],user_request=user)
    return Request.objects.last()

