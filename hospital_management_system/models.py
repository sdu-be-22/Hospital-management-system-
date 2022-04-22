from datetime import date
from django.db import models


class Patient(models.Model):
    first_name=models.CharField(max_length=100,null=False,blank=False)
    last_name=models.CharField(max_length=100,null=False,blank=False)
    email=models.EmailField(max_length=100)
    blood_pressure=models.IntegerField(null=False,default=0)
    heart_beat=models.IntegerField(null=False,default=0)
    haemoglobin=models.IntegerField(null=False,default=0)
    sugar=models.IntegerField(null=False,default=0)
    mod_date = models.DateField(default=date.today)

    def __str__(self):
        return self.first_name





class Appointment(models.Model): 
    STATUS=( 
          ('Aruzhan Askar','Aruzhan Askar'), 
          ('Dosbol Bekgali','Dosbol Bekgali'), 
          ('Nick Adel','Nick Adel'), 
          ('Lucy Andro','Lucy Andro'), 
          ('Aleksey Sergey','Aleksey Sergey'), 
          ('Nikolas Spark','Nikolas Spark'), 
          ('Samat Kozhagul','Samat Kozhagul'), 
          ('Alma Serikkyzy','Alma Serikkyzy'), 
      )

    STATUS_CHOICES = [
        ('Not Completed', 'Not Completed'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
        ('Postponed', 'Postponed'),
    ] 
    first_name=models.CharField(max_length=100,null=False,blank=False) 
    last_name=models.CharField(max_length=100) 
    age=models.CharField(max_length=3) 
    doctor=models.CharField(max_length=50, null=True, choices=STATUS,default='Doctor1') 
    email=models.EmailField(max_length=100) 
    app_date = models.DateField(default=date.today)
    time=models.TimeField() 
    status = models.CharField(max_length=14,choices=STATUS_CHOICES,default='Not Completed',)
    def __str__(self): 
         return self.first_name

class contactus(models.Model):
   Name=models.CharField(max_length=100)
   Email=models.EmailField(max_length=100)
   comment=models.TextField(max_length=500)

class Medicine(models.Model):
  name = models.CharField(max_length=200)
  cost = models.IntegerField()
  amount = models.IntegerField()
  ill=models.CharField(max_length=200)


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.name


class Doctors(models.Model):
    STATUS = (
			('Pediatrician', 'Pediatrician'),
			('Neurosurgeon', 'Neurosurgeon'),
			('Radiologist', 'Radiologist'),
            ('Mammologist', 'Mammologist'),
			('Dermatologist', 'Dermatologist'),
            ('Vascular Surgeon', 'Vascular Surgeon'),
			('Ophthalmologist', 'Ophthalmologist'),
			('Optometrist', 'Optometrist'),
			)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False,default='')
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age = models.IntegerField()
    speciality = models.CharField(max_length=50, null=True, choices=STATUS)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    university = models.CharField(max_length=500)
    experience = models.CharField(max_length=500)
    awards = models.CharField(max_length=500)
    description = models.TextField(null=False, default='')

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from datetime import datetime

# Create your views here.

class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

