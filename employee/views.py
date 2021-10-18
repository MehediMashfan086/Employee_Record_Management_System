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
            User.object.create_user(first_name = fn, last_name = ln, username = em, password = pwd)
            EmployeeInfo.objects.create(employeecode = ec)
        except:
            error = "Yes"
    
    return render(request, 'registration.html')
