from unicodedata import name
from django.urls import path
from .import views


urlpatterns =[
    path('',views.home,name="home"),

    path('register',views.register,name='register'),
    path('login/', views.login, name='login'),
    path('logout', views.logoutuser, name='logout'),

    path('doctor-dashboard',views.doctor_dashboard,name="doctor-dashboard"),

    path('patient-list', views.patients_list, name='patient-list'),
    path('create-patient', views.create_patient, name='create-patient'),
    path('edit_patient/<int:id>', views.edit_patient, name='edit-patient'),
    path('delete/<int:id>', views.delete_patient, name='delete-patient'),

    path('doctor-list', views.doctors_list, name='doctor-list'),
    path('create-doctor', views.create_doctor, name='create-doctor'),
    path('edit_doctor/<int:id>', views.edit_doctor, name='edit-doctor'),
    path('delete_doctor/<int:id>', views.delete_doctor, name='delete-doctor'),

    path('appointment-list',views.appointment_list,name='appointment-list'),
    path('patient-book-appointment',views.book_appointment,name="patient-book-appointment"),

    path('postpone/<int:id>',views.appointment_postpone,name="appointment-edit"),
    path('notcompleted/<int:id>',views.appointment_notcompleted,name='notcompleted'),
    path('cancel/<int:id>',views.appointment_cancel,name="cancel"),
    path('completed/<int:id>',views.appointment_completed,name="completed"),


    path('export-csv',views.export_csv,name='export-csv'),
    path('export-excel',views.export_excel,name='export-excel'),


    path('doctor_profile/<str:pk>/', views.doctor_profileView, name='doctor-profile'),
    path('doctor_grid',views.doctor_grid,name="doctor-grid"),


    path('todo/', views.todo, name='todo'),
    path('update_task/<str:pk>', views.updateTask, name='update-task'),
    path('delete_task/<str:pk>', views.deleteTask, name='delete-task'),

    path('all_appointments/',views.all_appointments,name="all-appointments"),
    path('all_doctors/',views.all_doctors,name="all-doctors"),
    path('chat', views.chat, name='chat'),



    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    
]
