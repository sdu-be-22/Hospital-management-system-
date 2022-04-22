from django import forms
from django.forms import ModelForm
from .models import  *


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name','last_name', 'email','blood_pressure','heart_beat','haemoglobin','sugar')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'blood_pressure':forms.NumberInput(attrs={'class':'form-control','placeholder':'Blood Pressure'}),
            'heart_beat':forms.NumberInput(attrs={'class':'form-control','placeholder':'Heart Beat'}),
            'haemoglobin':forms.NumberInput(attrs={'class':'form-control','placeholder':'Haemoglobin'}),
            'sugar':forms.NumberInput(attrs={'class':'form-control','placeholder':'Sugar'}),

        }

class DoctorForm(ModelForm):
    class Meta:
        model = Doctors
        fields = ('first_name','last_name', 'age','speciality','phone','email','gender','university','experience','awards')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'speciality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Speciality'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gender'}),
            'university': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'University'}),
            'experience': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Experience'}),
            'awards': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Awards(Certificates)'}),
        }

class AppointmentForm(ModelForm):
    class Meta:
        model=Appointment
        fields = ('first_name','last_name', 'age','doctor','email','app_date','time')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'doctor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose Doctor'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': ' Date '}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Time'}),
        }

class TaskForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))

	class Meta:
		model = Task
		fields = '__all__'
