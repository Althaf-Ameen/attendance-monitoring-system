from django.db import models
class student(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    doj = models.DateField(null=True, blank=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=True)
    leave_count = models.IntegerField(null=True, blank=True, default=0)
    on_leave = models.BooleanField(default=False)
class student_attendence(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    attendence= models.IntegerField(max_length=1,null=True,default=1)
    
# Create your models here.
