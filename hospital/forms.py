from django import forms
from django.contrib.auth.models import User
from hospital.models import *


class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['first_name','last_name','email','category','mobile','profile_pic']
        # exclude = ('user',) # won't work
       
        

class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields = ['first_name','last_name','email','profile_pic']
     





class TaskForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))

	class Meta:
		model = Task
		fields = '__all__'


class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model=Doctor
        exclude = ('user', 'status') # won't work
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'speciality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Speciality'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gender'}),
            'university': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'University'}),
            'experience': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Experience'}),
            'awards': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Awards(Certificates)'}),
            
        }

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model=Patient
        exclude = ('user','status','mod_date') # won't work
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'blood_pressure':forms.NumberInput(attrs={'class':'form-control','placeholder':'Blood Pressure'}),
            'heart_beat':forms.NumberInput(attrs={'class':'form-control','placeholder':'Heart Beat'}),
            'haemoglobin':forms.NumberInput(attrs={'class':'form-control','placeholder':'Haemoglobin'}),
            'sugar':forms.NumberInput(attrs={'class':'form-control','placeholder':'Sugar'}),

        }
