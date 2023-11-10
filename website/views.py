from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddPatientForm, AddDoctorForm, AddRequestForm, RoomForm, BedForm, AddInPatientForm
from .models import Patient, Doctor,Room, Bed, InPatient, Request



# General view requests
def home(request):
	patients = Patient.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Login Sucessful")
			return redirect('home')
		else:
			messages.success(request, "Error Logging in")
			return redirect('home')
	else:
		return render(request, 'home.html', {'patients':patients})



def logout_user(request):
	logout(request)
	messages.success(request, "Logout Sucessful")
	return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Login Sucessfull")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


# Patient Management System

def see_patient_management(request):
	if request.user.is_authenticated:
		return render(request, 'patient_managements/patient_management.html', {})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')

# Patient view requests

def see_patient_table(request):
	if request.user.is_authenticated:
		patients = Patient.objects.all()
		return render(request, 'patient_managements/patient_table.html', {'patients':patients})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')



def patient_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Patients
		patient_record = Patient.objects.get(SSN=pk)
		return render(request, 'patient_managements/patient.html', {'patient_record':patient_record})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')



def delete_patient(request, pk):
	if request.user.is_authenticated:
		delete_it = Patient.objects.get(SSN=pk)
		delete_it.delete()
		messages.success(request, "Patient record deleted")
		return redirect('patient_table')
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')


def add_patient(request):
	form = AddPatientForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_patient = form.save()
				messages.success(request, "Patient Added...")
				return redirect('patient_table')
		return render(request, 'patient_managements/add_patient.html', {'form':form})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')


def update_patient(request, pk):
	if request.user.is_authenticated:
		current_patient = Patient.objects.get(SSN=pk)
		form = AddPatientForm(request.POST or None, instance=current_patient)
		if form.is_valid():
			form.save()
			messages.success(request, "Patient record updated.")
			return redirect('patient_table')
		return render(request, 'patient_managements/update_patient.html', {'form':form})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')
	



# Doctor view requests

def see_doctor_table(request):
	if request.user.is_authenticated:
		doctors = Doctor.objects.all()
		return render(request, 'patient_managements/doctor_table.html', {'doctors':doctors})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')


def doctor_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Patients
		doctor_record = Doctor.objects.get(id=pk)
		return render(request, 'patient_managements/doctor.html', {'doctor_record':doctor_record})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')



def delete_doctor(request, pk):
	if request.user.is_authenticated:
		delete_it = Doctor.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Doctor record deleted")
		return redirect('doctor_table')
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')


def add_doctor(request):
	form = AddDoctorForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_doctor = form.save()
				messages.success(request, "Doctor Added...")
				return redirect('doctor_table')
		return render(request, 'patient_managements/add_doctor.html', {'form':form})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')


def update_doctor(request, pk):
	if request.user.is_authenticated:
		current_doctor = Doctor.objects.get(id=pk)
		form = AddDoctorForm(request.POST or None, instance=current_doctor)
		if form.is_valid():
			form.save()
			messages.success(request, "Doctor record updated.")
			return redirect('doctor_table')
		return render(request, 'patient_managements/update_doctor.html', {'form':form})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')
	

	# In-Patient Management System

def see_in_patient_management(request):
    if request.user.is_authenticated:
        return render(request, 'in_patient_managements/in_patient_management.html', {})
    else:
        messages.success(request, "This action requires the user to be logged in.")
        return redirect('home')
	



# Request view requests

def see_request_table(request):
	if request.user.is_authenticated:
		requests = Request.objects.all()
		return render(request, 'patient_managements/request_table.html', {'requests':requests})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')

def request_record(request, pk):
	if request.user.is_authenticated:
		request_record = Request.objects.get(id=pk)
		return render(request, 'patient_managements/request.html', {'request_record':request_record})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')

def see_illness_table(request):
	if request.user.is_authenticated:
		illness = Illness.objects.all()
		return render(request, 'patient_managements/illness_table.html', {'illness':illness})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')

def delete_request(request, pk):
	if request.user.is_authenticated:
		delete_it = Request.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Request record deleted")
		return redirect('request_table')
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')


def add_request(request):
	form = AddRequestForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_request = form.save()
				messages.success(request, "Request Added...")
				return redirect('request_table')
		return render(request, 'patient_managements/add_request.html', {'form':form})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')


def update_request(request, pk):
	if request.user.is_authenticated:
		current_request = Request.objects.get(id=pk)
		form = AddRequestForm(request.POST or None, instance=current_request)
		if form.is_valid():
			form.save()
			messages.success(request, "Request record updated.")
			return redirect('request_table')
		return render(request, 'patient_managements/update_request.html', {'form':form})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')

def illness_record(request, pk):
	if request.user.is_authenticated:
		illness_record = Illness.objects.get(id=pk)
		return render(request, 'patient_managements/illness.html', {'illness_record':illness_record})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')


def delete_illness(request, pk):
	if request.user.is_authenticated:
		delete_it = Illness.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Illness record deleted")
		return redirect('illness_table')
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')


def add_illness(request):
	form = AddIllnessForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_illness = form.save()
				messages.success(request, "Illness Added...")
				return redirect('illness_table')
		return render(request, 'patient_managements/add_illness.html', {'form':form})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')


def update_illness(request, pk):
	if request.user.is_authenticated:
		current_illness = Illness.objects.get(id=pk)
		form = AddIllnessForm(request.POST or None, instance=current_illness)
		if form.is_valid():
			form.save()
			messages.success(request, "Illness record updated.")
			return redirect('illness_table')
		return render(request, 'patient_managements/update_illness.html', {'form':form})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')


# Medical History view requests

def see_medicalhistory_table(request):
	if request.user.is_authenticated:
		Medical History = MedicalHistory.objects.all()
		return render(request, 'patient_managements/medicalhistory_table.html', {'medical history':medical history})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')

def medicalhistory_record(request, pk):
	if request.user.is_authenticated:
		medicalhistory_record = MedicalHistory.objects.get(id=pk)
		return render(request, 'patient_managements/illness.html', {'medicalhistory_record':medicalhistory_record})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')


def delete_medicalhistory(request, pk):
	if request.user.is_authenticated:
		delete_it = MedicalHistory.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Medical History record deleted")
		return redirect('medicalhistory_table')
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')


def add_medicalhistory(request):
	form = AddMedicalHistoryForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_medicalhistory = form.save()
				messages.success(request, "Medical History Added...")
				return redirect('medicalhistory_table')
		return render(request, 'patient_managements/add_medicalhistory.html', {'form':form})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')


def update_medicalhistory(request, pk):
	if request.user.is_authenticated:
		current_medicalhistory = MedicalHistory.objects.get(id=pk)
		form = AddMedicalHistoryForm(request.POST or None, instance=current_medicalhistory)
		if form.is_valid():
			form.save()
			messages.success(request, "Medical History record updated.")
			return redirect('medicalhistory_table')
		return render(request, 'patient_managements/update_medicalhistory.html', {'form':form})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')


# Request view requests

def see_request_table(request):
	if request.user.is_authenticated:
		Request = Request.objects.all()
		return render(request, 'patient_managements/request_table.html', {'request':request})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')

def request_record(request, pk):
	if request.user.is_authenticated:
		request_record = Request.objects.get(id=pk)
		return render(request, 'patient_managements/request.html', {'request_record':request_record})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')


def delete_request(request, pk):
	if request.user.is_authenticated:
		delete_it = Request.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Request record deleted")
		return redirect('request_table')
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')


def add_request(request):
	form = AddRequestForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_request = form.save()
				messages.success(request, "Request Added...")
				return redirect('request_table')
		return render(request, 'patient_managements/add_request.html', {'form':form})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')


def update_request(request, pk):
	if request.user.is_authenticated:
		current_request = Request.objects.get(id=pk)
		form = AddRequestForm(request.POST or None, instance=current_request)
		if form.is_valid():
			form.save()
			messages.success(request, "Request record updated.")
			return redirect('request_table')
		return render(request, 'patient_managements/update_request.html', {'form':form})
	else:
		messages.success(request, "This action requres user to be logged in.")
		return redirect('home')



# Room view requests

def see_room_table(request):
    if request.user.is_authenticated:
        rooms = Room.objects.all()
        return render(request, 'in_patient_managements/room_table.html', {'rooms': rooms})
    else:
        messages.success(request, "This action requires the user to be logged in.")
        return redirect('home')

def room_record(request, pk):
    if request.user.is_authenticated:
        room_record = Room.objects.get(id=pk)
        return render(request, 'in_patient_managements/room.html', {'room_record': room_record})
    else:
        messages.success(request, "This action requires the user to be logged in.")
        return redirect('home')

def delete_room(request, pk):
    if request.user.is_authenticated:
        delete_it = Room.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Room record deleted")
        return redirect('room_table')
    else:
        messages.success(request, "This action requires the user to be logged in.")
        return redirect('home')

def add_room(request):
    form = RoomForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_room = form.save()
                messages.success(request, "Room Added...")
                return redirect('room_table')
        return render(request, 'in_patient_managements/add_room.html', {'form': form})
    else:
        messages.success(request, "This action requires the user to be logged in.")
        return redirect('home')

def update_room(request, pk):
    if request.user.is_authenticated:
        current_room = Room.objects.get(id=pk)
        form = RoomForm(request.POST or None, instance=current_room)
        if form.is_valid():
            form.save()
            messages.success(request, "Room record updated.")
            return redirect('room_table')
        return render(request, 'in_patient_managements/update_room.html', {'form': form})
    else:
        messages.success(request, "This action requires the user to be logged in.")
        return redirect('home')


# Bed view requests

def see_bed_table(request):
    if request.user.is_authenticated:
        beds = Bed.objects.all()
        return render(request, 'in_patient_managements/bed_table.html', {'beds': beds})
    else:
        messages.success(request, "This action requires the user to be logged in.")
        return redirect('home')

def bed_record(request, pk):
    if request.user.is_authenticated:
        bed_record = Bed.objects.get(id=pk)
        return render(request, 'in_patient_managements/bed.html', {'bed_record': bed_record})
    else:
        messages.success(request, "This action requires the user to be logged in.")
        return redirect('home')

def delete_bed(request, pk):
    if request.user.is_authenticated:
        delete_it = Bed.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Bed record deleted")
        return redirect('bed_table')
    else:
        messages.success(request, "This action requires the user to be logged in.")
        return redirect('home')

def add_bed(request):
    form = BedForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_bed = form.save()
                messages.success(request, "Bed Added...")
                return redirect('bed_table')
        return render(request, 'in_patient_managements/add_bed.html', {'form': form})
    else:
        messages.success(request, "This action requires the user to be logged in.")
        return redirect('home')

def update_bed(request, pk):
    if request.user.is_authenticated:
        current_bed = Bed.objects.get(id=pk)
        form = BedForm(request.POST or None, instance=current_bed)
        if form.is_valid():
            form.save()
            messages.success(request, "Bed record updated.")
            return redirect('bed_table')
        return render(request, 'in_patient_managements/update_bed.html', {'form': form})
    else:
        messages.success(request, "This action requires the user to be logged in.")
        return redirect('home')
	


# InPatient Views

# InPatient Management System

def see_inpatient_management(request):
    if request.user.is_authenticated:
        return render(request, 'patient_managements/inpatient_management.html', {})
    else:
        messages.success(request, "This action requires the user to be logged in.")
        return redirect('home')

# InPatient view requests

def see_inpatient_table(request):
    if request.user.is_authenticated:
        inpatients = InPatient.objects.all()
        return render(request, 'in_patient_managements/inpatient_table.html', {'inpatients': inpatients})
    else:
        messages.success(request, "This action requires the user to be logged in.")
        return redirect('home')

def inpatient_record(request, pk):
    if request.user.is_authenticated:
        inpatient_record = InPatient.objects.get(id=pk)
        return render(request, 'in_patient_managements/inpatient.html', {'inpatient_record': inpatient_record})
    else:
        messages.success(request, "This action requires the user to be logged in.")
        return redirect('home')

def delete_inpatient(request, pk):
    if request.user.is_authenticated:
        delete_it = InPatient.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "InPatient record deleted")
        return redirect('inpatient_table')
    else:
        messages.success(request, "This action requires the user to be logged in.")
        return redirect('home')

def add_inpatient(request):
    form = AddInPatientForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_inpatient = form.save()
                messages.success(request, "InPatient Added...")
                return redirect('inpatient_table')
        return render(request, 'in_patient_managements/add_inpatient.html', {'form': form})
    else:
        messages.success(request, "This action requires the user to be logged in.")
        return redirect('home')

def update_inpatient(request, pk):
    if request.user.is_authenticated:
        current_inpatient = InPatient.objects.get(id=pk)
        form = AddInPatientForm(request.POST or None, instance=current_inpatient)
        if form.is_valid():
            form.save()
            messages.success(request, "InPatient record updated.")
            return redirect('inpatient_table')
        return render(request, 'in_patient_managements/update_inpatient.html', {'form': form})
    else:
        messages.success(request, "This action requires the user to be logged in.")
        return redirect('home')

