from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EmployeeInfo(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    employeecode = models.CharField(max_length=50)
    department = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=50, null=True)
    joiningdate = models.DateField(null= True)

    def __str__(self):
        return self.user.username 