from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctors)
admin.site.register(Appointment)
admin.site.register(Medicine)
admin.site.register(Category)