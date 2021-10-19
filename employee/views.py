from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['employeecode']
        em = request.POST['emailid']
        pwd = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name = fn, last_name = ln, username = em, password = pwd)
            EmployeeInfo.objects.create(user = user, employeecode = ec)
            error = "no"
        except:
            error = "yes"
    return render(request, 'registration.html', locals())

def emp_login(request):
    return render(request, 'emp_login.html')
