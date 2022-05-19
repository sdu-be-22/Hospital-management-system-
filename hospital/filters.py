import django_filters
from .models import *

class DoctorsFilter(django_filters.FilterSet):
    class Meta:
        model = Doctor
        fields = ('first_name','category')
