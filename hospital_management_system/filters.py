from dataclasses import fields
import django_filters

from .models import *

class DoctorsFilter(django_filters.FilterSet):
    class Meta:
        model = Doctors
        fields = ('first_name','speciality')


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Medicine
        fields = '__all__'