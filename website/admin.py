from django.contrib import admin
from .models import Patient,Doctor,Nurse,MedicalHistory, Illness,Request,Bed,Room,InPatient




admin.site.register(Patient)

admin.site.register(Physician)

admin.site.register(Surgeon)

admin.site.register(Nurse)

admin.site.register(Illness)

admin.site.register(MedicalHistory)

admin.site.register(Request)

admin.site.register(Medication)

admin.site.register(Bed)

admin.site.register(Room)

admin.site.register(InPatient)