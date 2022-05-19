from django.db import models
from datetime import date, datetime
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.name

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    mobile = models.CharField(max_length=20,null=True)
    status=models.BooleanField(default=False)
    university = models.CharField(max_length=500,default='')
    experience = models.CharField(max_length=500,default='')
    awards = models.CharField(max_length=500,default='')
    description = models.TextField(null=False, default='')
    number = models.IntegerField(null=False,default=0)
    gender = models.CharField(max_length=40,default='')



class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    first_name=models.CharField(max_length=40,default='')
    last_name=models.CharField(max_length=40,default='')
    email = models.EmailField(max_length=50)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    mobile = models.CharField(max_length=20,null=False)
    mod_date = models.DateField(default=date.today)
    status=models.BooleanField(default=False)
    blood_pressure=models.IntegerField(null=False,default=0)
    heart_beat=models.IntegerField(null=False,default=0)
    haemoglobin=models.IntegerField(null=False,default=0)
    sugar=models.IntegerField(null=False,default=0)
    temp=models.IntegerField(null=False,default=0)
    number = models.IntegerField(null=False,default=0)
    gender = models.CharField(max_length=40,default='')


class Appointment(models.Model): 
    DOCTOR=( 
          ('Aruzhan Askar','Aruzhan Askar'), 
          ('Dosbol Bekgali','Dosbol Bekgali'), 
          ('Nick Adel','Nick Adel'), 
          ('Lucy Andro','Lucy Andro'), 
          ('Aleksey Sergey','Aleksey Sergey'), 
          ('Nikolas Spark','Nikolas Spark'), 
          ('Samat Kozhagul','Samat Kozhagul'), 
          ('Alma Serikkyzy','Alma Serikkyzy'), 
    )
    STATUS= [
        ('Not Completed', 'Not Completed'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
        ('Postponed', 'Postponed'),
    ] 
    first_name=models.CharField(max_length=20,null=False,blank=False) 
    last_name=models.CharField(max_length=20) 
    age=models.CharField(max_length=3) 
    doctor=models.CharField(max_length=30, null=True, choices=DOCTOR,default='Doctor1') 
    email=models.EmailField(max_length=20) 
    app_date = models.DateField(default=date.today)
    time=models.TimeField() 
    status = models.CharField(max_length=14,choices=STATUS,default='Not Completed')
    def __str__(self): 
        return self.first_name

class Room(models.Model):
    name = models.CharField(max_length=1000)

    
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

class Task(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    def __str__(self): 
        return self.title

class Appointment(models.Model): 
    DOCTOR=( 
          ('Aruzhan Askar','Aruzhan Askar'), 
          ('Dosbol Bekgali','Dosbol Bekgali'), 
          ('Nick Adel','Nick Adel'), 
          ('Lucy Andro','Lucy Andro'), 
          ('Aleksey Sergey','Aleksey Sergey'), 
          ('Nikolas Spark','Nikolas Spark'), 
          ('Samat Kozhagul','Samat Kozhagul'), 
          ('Alma Serikkyzy','Alma Serikkyzy'), 
    )
    STATUS= [
        ('Not Completed', 'Not Completed'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
        ('Postponed', 'Postponed'),
    ] 
    first_name=models.CharField(max_length=20,null=False,blank=False) 
    last_name=models.CharField(max_length=20) 
    age=models.CharField(max_length=3) 
    doctor=models.CharField(max_length=30, null=True, choices=DOCTOR,default='Doctor1') 
    email=models.EmailField(max_length=20) 
    app_date = models.DateField(default=date.today)
    time=models.TimeField() 
    status = models.CharField(max_length=14,choices=STATUS,default='Not Completed')
    def __str__(self): 
        return self.first_name

