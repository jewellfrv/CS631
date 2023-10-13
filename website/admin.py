from django.contrib import admin
from .models import Patient,Doctor,Bed,Room,InPatient

admin.site.register(Patient)

admin.site.register(Doctor)

admin.site.register(Bed)

admin.site.register(Room)

admin.site.register(InPatient)