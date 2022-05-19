from django.contrib import admin

from hospital.models import *


admin.site.register(Doctor)
admin.site.register(Category)
admin.site.register(Patient)
admin.site.register(Task)
admin.site.register(Appointment)