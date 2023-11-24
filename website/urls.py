from django.urls import path
from . import views


urlpatterns = [
    # General URLs
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    # Patient Management URLs

    path('patient_management/', views.see_patient_management, name='patient_management'),

    # Patient URLs
    path('patient_management/patient_table/', views.see_patient_table, name='patient_table'),
    path('patient_management/patient<int:pk>', views.patient_record, name='patient'),
    path('patient_management/delete_patient<int:pk>', views.delete_patient, name='delete_patient'),
    path('patient_management/add_patient/', views.add_patient, name='add_patient'),
    path('patient_management/update_patient/<int:pk>', views.update_patient, name='update_patient'),


    # Physician URLs
    path('patient_management/physician_table/', views.see_physician_table, name='physician_table'),
    path('patient_management/physician<int:pk>', views.physician_record, name='physician'),
    path('patient_management/delete_physician<int:pk>', views.delete_physician, name='delete_physician'),
    path('patient_management/add_physician/', views.add_physician, name='add_physician'),
    path('patient_management/update_physician/<int:pk>', views.update_physician, name='update_physician'),


   # Surgeon URLs
    path('patient_management/surgeon_table/', views.see_surgeon_table, name='surgeon_table'),
    path('patient_management/surgeon<int:pk>', views.surgeon_record, name='surgeon'),
    path('patient_management/delete_surgeon<int:pk>', views.delete_surgeon, name='delete_surgeon'),
    path('patient_management/add_surgeon/', views.add_surgeon, name='add_surgeon'),
    path('patient_management/update_surgeon/<int:pk>', views.update_surgeon, name='update_surgeon'),


   # Nurse URLs
    path('patient_management/nurse_table/', views.see_nurse_table, name='nurse_table'),
    path('patient_management/nurse<int:pk>', views.nurse_record, name='nurse'),
    path('patient_management/delete_nurse<int:pk>', views.delete_nurse, name='delete_nurse'),
    path('patient_management/add_nurse/', views.add_nurse, name='add_nurse'),
    path('patient_management/update_nurse/<int:pk>', views.update_nurse, name='update_nurse'),




    # Request URLs
    path('patient_management/request_table/', views.see_request_table, name='request_table'),
    path('patient_management/request<int:pk>', views.request_record, name='request'),
    path('patient_management/delete_request<int:pk>', views.delete_request, name='delete_request'),
    path('patient_management/add_request/', views.add_request, name='add_request'),
    path('patient_management/update_request/<int:pk>', views.update_request, name='update_request'),

    # Medical History URLs
    path('patient_management/medicalhistory_table/', views.see_medicalhistory_table, name='medicalhistory_table'),
    path('patient_management/medicalhistory<int:pk>', views.medicalhistory_record, name='medicalhistory'),
    path('patient_management/delete_medicalhistory<int:pk>', views.delete_medicalhistory, name='delete_medicalhistory'),
    path('patient_management/add_medicalhistory/', views.add_illness, name='add_medicalhistory'),
    path('patient_management/update_medicalhistory/<int:pk>', views.update_illness, name='update_medicalhistory'),


    # Request URLs
    path('patient_management/request_table/', views.see_request_table, name='request_table'),
    path('patient_management/request<int:pk>', views.request_record, name='request'),
    path('patient_management/delete_request<int:pk>', views.delete_request, name='delete_request'),
    path('patient_management/add_request/', views.add_request, name='add_request'),
    path('patient_management/update_request/<int:pk>', views.update_request, name='update_request'),

    
    # In_Patient Management URLs
    path('in_patient_management/', views.see_in_patient_management, name='in_patient_management'),

    # Bed URLs
    path('in_patient_management/bed_table/', views.see_bed_table, name='bed_table'),
    path('in_patient_management/bed<int:pk>', views.bed_record, name='bed'),
    path('in_patient_management/delete_bed<int:pk>', views.delete_bed, name='delete_bed'),
    path('in_patient_management/add_bed/', views.add_bed, name='add_bed'),
    path('in_patient_management/update_bed/<int:pk>', views.update_bed, name='update_bed'),


    # Room URLs
    path('in_patient_management/room_table/', views.see_room_table, name='room_table'),
    path('in_patient_management/room<int:pk>', views.room_record, name='room'),
    path('in_patient_management/delete_room<int:pk>', views.delete_room, name='delete_room'),
    path('in_patient_management/add_room/', views.add_room, name='add_room'),
    path('in_patient_management/update_room/<int:pk>', views.update_room, name='update_room'),

    # InPatient URLs
    path('in_patient_management/inpatient_table/', views.see_inpatient_table, name='inpatient_table'),
    path('in_patient_management/inpatient<int:pk>', views.inpatient_record, name='inpatient'),
    path('in_patient_management/delete_inpatient<int:pk>', views.delete_inpatient, name='delete_inpatient'),
    path('in_patient_management/add_inpatient/', views.add_inpatient, name='add_inpatient'),
    path('in_patient_management/update_inpatient/<int:pk>', views.update_inpatient, name='update_inpatient'),




]