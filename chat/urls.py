
from django.urls import path, include
from . import views

urlpatterns = [
    path('chat_doctor', views.chat_doctor, name='chat_doctor'),
    path('chat_patient', views.chat_patient, name='chat_patient'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]