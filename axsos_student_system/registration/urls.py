from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login',views.login),
    path('student_profile',views.student),
    path('request',views.request),
    path('logout',views.logout),
    path('instructor',views.instructor),
    path('attendance',views.attendance),
    path('tickets',views.tickets),
]
