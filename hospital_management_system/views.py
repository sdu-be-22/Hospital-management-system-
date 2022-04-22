from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date, timedelta
from django.http import HttpResponse, JsonResponse 
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User , auth
from django.contrib.auth import  logout

from hospital_management_system.serializers import *
from .forms import AppointmentForm, DoctorForm,PatientForm, TaskForm

from .models import  *
from django.conf import settings 
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .filters import  DoctorsFilter
from django.contrib.auth.decorators import login_required
import csv
import xlwt

from .my_captcha import FormWithCaptcha
#------------------------ HOME PAGE ----------------------------------------------
#---------------------------------------------------------------------------------
def home(request):
   return render(request,'../templates/index.html',{})


#lOGIN
def login(request):
   if request.method == 'POST':
      username=request.POST['username'] 
      password1=request.POST['password']

      user = auth.authenticate(username=username, password=password1)
      if user is not None:
             auth.login(request, user)
             print('you are logged in')
             return redirect('doctor-dashboard')
      else:
            print('incorrect')
            messages.info(request, 'Username or password is incorrect')
            return redirect('login')
   else:
        return render(request,'calc/login.html')
#LOGOUT
def logoutuser(request):
	logout(request)
	return redirect('login')

#REGISTER
def register(request):
   if request.method == 'POST':
      username=request.POST['username']
      first_name=request.POST['first_name']
      last_name=request.POST['last_name']
      email=request.POST['email']
      password1=request.POST['password1']
      password2=request.POST['password2']

      username=request.POST.get('username')
      first_name=request.POST.get('first_name')
      last_name=request.POST.get('last_name')
      email=request.POST.get('email')

      if password1==password2:
         if User.objects.filter(username=username).exists():
            print('Username taken')
            messages.info(request,'Username  taken')
            return redirect('register')
            
         else :
            user=User.objects.create_user(username=username,password=password1,last_name=last_name,email=email,first_name=first_name)
            user.save();
            html_content =render_to_string("calc/welcome.html",{'title':'Welcome to The TrustyMed','first_name':first_name})
            text_content = strip_tags(html_content)
            send_email=EmailMultiAlternatives(
                #subject
                'Welcome to The TrustyMed',
                #content 
                text_content,
                #from email
                settings.EMAIL_HOST_USER,
                #rec list
                [email],
             )
            send_email.attach_alternative(html_content,"text/html")
            send_email.send()
            # new_patient=Patient(first_name=first_name,email=email,last_name=last_name)
            # new_patient.save()
            messages.success(request,'User '+username+' created ')
            print('user created')
            return redirect ('login')
      else:
         print('password not match')
         messages.info(request,'Password not match')
         return redirect('register')
   else:
      return render(request,'calc/register.html',{})




#---------------------------------------------------------------------------------
#------------------------ DOCTOR RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------

#DOCTOR DASHBOARD
@login_required(login_url='login')
def doctor_dashboard(request):
   patients=Patient.objects.all()
   num_of_patients=patients.count
   appointment= Appointment.objects.all().count

   completed= Appointment.objects.filter(status='Completed').count
   notcompleted= Appointment.objects.filter(status='Not Completed').count
   postponed= Appointment.objects.filter(status='Postponed').count
   canceled= Appointment.objects.filter(status='Canceled').count
   num_of_patients_today=patients.filter(mod_date=date.today()).count
   tasks = Task.objects.all()
   form = TaskForm()
   if request.method=='POST':
      form=TaskForm(request.POST)
      if form.is_valid():
         form.save()
      return redirect('doctor-dashboard')
   context={
      'patients':patients,
      'num_of_patients':num_of_patients,
      'num_of_patients_today':num_of_patients_today,
      'appointment':appointment,
      'tasks': tasks, 
      'form': form,
      'completed':completed,
      'notcompleted':notcompleted,
      'postponed':postponed,
      'canceled':canceled,
   }
   return render(request,'calc/doctor_dashboard.html',context)





# LIST OF THE PATIENTS
@login_required(login_url='login')
def patients_list(request):
   patients=Patient.objects.all()
   num_of_patients=patients.count
   appointment= Appointment.objects.all().count
   num_of_patients_today=patients.filter(mod_date=date.today()).count
   context={
      'patients':patients,
      'num_of_patients':num_of_patients,
      'num_of_patients_today':num_of_patients_today,
      'appointment':appointment,
   }
   return render(request, 'calc/patient_list.html', context)

# CREATE NEW PATIENT
@login_required(login_url='login')
def create_patient(request):
   form=PatientForm()
   if request.method=='POST':
      form=PatientForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('patients-list')

   context={
      'form':form,
   }
   return render(request, 'calc/create.html', context)

# EDIT PATIENT INFORMATION
@login_required(login_url='login')
def edit_patient(request,id):
   patient = Patient.objects.get(id=id)
   form = PatientForm(instance=patient)
   if request.method == 'POST':
        form = PatientForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient-list')  
   context = {
        'patient':patient,
        'form': form,
   }
   return render(request, 'calc/edit.html',context)

# DELETE PATIENT 
@login_required(login_url='login')
def delete_patient(request,id):
   patient = Patient.objects.get(id=id)
   patient.delete()
   return redirect('patient-list')




#------------------------ PATIENT RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------



# APPOINTMENTS LIST
@login_required(login_url=' login ')
def appointment_list(request):
   appointments=Appointment.objects.all()
   appointments_today=Appointment.objects.filter(app_date=date.today()).count
   if request.method=='POST':
      if request.POST.get('today'):
            today= appointments.filter(app_date=date.today())
            context={
            'appointments' :today,
            'appointments_today':appointments_today
            }
      elif request.POST.get('all'):
         context={
         'appointments':appointments,
         'appointments_today':appointments_today
         
         }
      else:
         date_today = date.today()
         date_upc=date_today + timedelta(days=1)
         upcom=appointments.filter(app_date=date_upc)
         context={ 
            'appointments' :upcom,
            'appointments_today':appointments_today
         }
   else:
      context={
      'appointments':appointments,
      'appointments_today':appointments_today
      }
   return render(request,'calc/appointment_list.html',context)


# def appointment_list(request):
#    appointments=Appointment.objects.all()
#    appointments_today=Appointment.objects.filter(app_date=date.today()).count
#    context={
#       'appointments':appointments,
#       'appointments_today':appointments_today
#    }
#    return render(request,'calc/appointment_list.html',context)



# EDIT APPOINTMENT DETAILS POSTPONE
@login_required(login_url='login')
def appointment_postpone(request,id):
   appointment = Appointment.objects.get(id=id)
   status_in = Appointment.objects.filter(id=id)
   if request.method == 'POST' :
      status_in = status_in.update(status = 'Postponed')
      return redirect('appointment-list')  
   return render(request, 'calc/edit.html',{'appointment':appointment,'status':status_in})


@login_required(login_url='login')
def appointment_completed(request,id):
   appointment = Appointment.objects.get(id=id)
   status_in = Appointment.objects.filter(id=id)
   if request.method == 'POST':
            status_in = status_in.update(status = 'Completed')
            return redirect('appointment-list')
   return render(request, 'calc/edit.html',{'appointment':appointment,'status':status_in})

@login_required(login_url='login')
def appointment_notcompleted(request,id):
   appointment=Appointment.objects.get(id=id)
   status_in=Appointment.objects.filter(id=id)  
   if request.method=='POST':
      status_in = status_in.update(status='Not Completed')
      return redirect('appointment-list')
   return render(request,'calc/edit.html',{'appointment':appointment,'status':status_in})

#CANCEL APPOINTMENTS
@login_required(login_url='login')
def appointment_cancel(request,id):
   appointment=Appointment.objects.get(id=id)
   status_in=Appointment.objects.filter(id=id)
   if request.method == 'POST':
      status_in = status_in.update(status = 'Canceled')
      return redirect('appointment-list')
   return render (request,'calc/edit.html',{'appointment':appointment,'status':status_in}) 




#---------------------------------------------------------------------------------
#------------------------ DOCTOR RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------





#---------------------------------------------------------------------------------
#------------------------ PATIENT RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
 
# Book an appointment
@login_required(login_url='login')
def book_appointment(request):
   form=AppointmentForm()
   doctors=Doctors.objects.all()
   if request.method=='POST':
      form=PatientForm(request.POST)
      first_name=request.POST['first_name']
      last_name=request.POST['last_name']
      age=request.POST['age']
      email=request.POST['email']
      doctor=request.POST['doctor']
      app_date=request.POST['date']
      time=request.POST['time']
      if form.is_valid():
         form.save()
         new_appointment=Appointment(first_name=first_name,last_name=last_name,age=age,email=email,doctor=doctor,app_date=app_date,time=time)
         new_appointment.save()
         return redirect('/')
   context={
      'form':form,
      'doctors':doctors
   }
   return render(request, 'calc/appointment.html', context)



#---------------------------------------------------------------------------------
#------------------------ ADMIN RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------


#DOCTOR'S LIST
def doctors_list(request):
   doctors=Doctors.objects.all()
   num_of_doctors=doctors.count
   myFilter=DoctorsFilter(request.GET, queryset=doctors)
   doctors = myFilter.qs
   context={
      'doctors':doctors,
      'num_of_doctors':num_of_doctors,
      'myFilter':myFilter,
   }
   return render(request, 'calc/doctor_list.html', context)

#ADD A NEW DOCTOR
@login_required(login_url='login')
def create_doctor(request):
   form=DoctorForm()
   if request.method=='POST':
      form=DoctorForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('doctor-list')

   context={
      'form':form,
   }
   return render(request, 'calc/create.html', context)

#EDIT DOCTOR INFORMATION
@login_required(login_url=' login ')
def edit_doctor(request,id):
   doctor = Doctors.objects.get(id=id)
   form = DoctorForm(instance=doctor)

   if request.method == 'POST':
        form = DoctorForm(request.POST,instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor-list')  

   context = {
        'doctor':doctor,
        'form': form,
   }
   return render(request, 'calc/edit.html',context)


#DELETE DOCTOR 
@login_required(login_url=' login ')
def delete_doctor(request,id):
   doctor = Doctors.objects.get(id=id)
   doctor.delete()
   return redirect('doctor-list')










def export_csv(request):
   response= HttpResponse(content_type='text/csv')
   response['Content-Disposition']='attachment; filename=Patients.csv '
   writer=csv.writer(response)
   patients=Patient.objects.all()
   writer.writerow(['First name','','Last name','','Email','','Blood Pressure'])
   for p in patients:
      writer.writerow([p.first_name,p.last_name, p.email, p.blood_pressure])
   return response





def export_excel(request):
   response= HttpResponse(content_type='application/ms-excel')
   response['Content-Disposition']='attachment; filename=Patients.xls '
   wb=xlwt.Workbook(encoding='utf-8')
   ws=wb.add_sheet('Patients')
   row_num=0
   font_style=xlwt.XFStyle()
   font_style.font.bold=True
   columns=['First name','Last name','Email','Blood Pressure']
   for col_num in range(len(columns)):
      ws.write(row_num,col_num,columns[col_num],font_style)
   font_style=xlwt.XFStyle()
   rows=Patient.objects.all().values_list('first_name','last_name', 'email', 'blood_pressure')

   for row in rows:
      row_num=row_num+1
      for col_num in range(len(row)):
         ws.write(row_num,col_num,str(row[col_num]),font_style)
   wb.save(response)
   return response


def doctor_grid(request):
    category = request.GET.get('category')
    if category == None:
        profiles = Doctors.objects.all()
    else:
        profiles = Doctors.objects.filter(category__name = category)


    categories = Category.objects.all()
    
    context = {'categories': categories, 'profiles' : profiles}
    return render(request, 'calc/doctor-grid.html', context)


def doctor_profileView(request, pk):
    profile = Doctors.objects.get(id=pk)
    return render(request, 'calc/doctor-profile.html', {'profile': profile})



def todo(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method=='POST':
            form=TaskForm(request.POST)
            if form.is_valid():
                    form.save()
            return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'calc/todo.html', context)


def updateTask(request, pk):
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('doctor-dashboard')

	context = {'form':form}

	return render(request, 'calc/update_task.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('doctor-dashboard')

    context={'item': item}
    return render(request, 'calc/delete.html', context)


@api_view()
def all_appointments(request):
  appointments = Appointment.objects.all()
  appointment_serializer = AppointmentSerializer(appointments, many=True)
  return Response(appointment_serializer.data)
@api_view()
def all_doctors(request):
   doctors=Doctors.objects.all()
   doctors_serializer= DoctorSerializer(doctors,many=True)
   return Response(doctors_serializer.data)


def chat(request):
    return render(request, 'calc/chat.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'calc/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

def chat_bot(request):
    return render(request, 'calc/chat_bot.html')

#---------------------------------------------------------------------------------
#------------------------ Medicines ------------------------------
#---------------------------------------------------------------------------------


def store(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False)
          items = OrderItem.objects.all()
          # cartItems = order.get_cart_items()
     else:
          items = []
          order = {'get_cart_total': 0, 'get_cart_items': 0,'shipping': False }
          cartItems = order['get_cart_items']

     products = Product.objects.all()
     context = {
          'products': products,
          # 'cartItems': cartItems
     }
     return render(request, 'store/store.html', context)

def robot(request):
    context = {
        "captcha": FormWithCaptcha,
    }
    return render(request, 'robot.html', context)
   
