from rest_framework import serializers

class AppointmentSerializer(serializers.Serializer):
 first_name=serializers.CharField()
 last_name=serializers.CharField()
 age=serializers.CharField()
 doctor=serializers.CharField()
 email=serializers.EmailField()
 time=serializers.TimeField()
 app_date=serializers.DateField()
 status=serializers.CharField()

class DoctorSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    age = serializers.IntegerField()
    speciality = serializers.CharField()
    phone =serializers.IntegerField()
    email = serializers.CharField()
    gender = serializers.CharField()
    university = serializers.CharField()
    experience = serializers.CharField()
    awards = serializers.CharField()
    description = serializers.CharField()