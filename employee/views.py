from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def index(request):
    return render(request, 'index.html')

def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['employeecode']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']
        try:
            user = User.objects.create_user(first_name = fn, last_name = ln, username = em, password = pwd)
            EmployeeInfo.objects.create(user = user, employeecode = ec)
            error = "no"
        except:
            error = "yes"
    return render(request, 'registration.html', locals())

def emp_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST.get('emailid')
        p = request.POST.get('passwd')
        user = authenticate(username = u, password = p)
        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"
    return render(request, 'emp_login.html', locals())

def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login.html')
    return render(request, 'emp_home.html')

def Logout(request):
    Logout(request)
    return redirect('index.html')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login.html')
    error = ""
    user = request.user
    employee = EmployeeInfo.objects.get(user=user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['employeecode']
        em = request.POST['email']
        pwd = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name = fn, last_name = ln, username = em, password = pwd)
            EmployeeInfo.objects.create(user = user, employeecode = ec)
            error = "no"
        except:
            error = "yes"
    return render(request, 'profile.html', locals())
