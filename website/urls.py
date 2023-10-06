from django.urls import path
from . import views


urlpatterns = [
    # General URLs
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),


    # Patient URLs
    path('patient_table/', views.see_patient_table, name='patient_table'),
    path('patient<int:pk>', views.patient_record, name='patient'),
    path('delete_patient<int:pk>', views.delete_patient, name='delete_patient'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('update_patient/<int:pk>', views.update_patient, name='update_patient'),


    # Doctor URLs
    path('doctor_table/', views.see_doctor_table, name='doctor_table'),
    path('doctor<int:pk>', views.doctor_record, name='doctor'),
    path('delete_doctor<int:pk>', views.delete_doctor, name='delete_doctor'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('update_doctor/<int:pk>', views.update_doctor, name='update_doctor'),

]