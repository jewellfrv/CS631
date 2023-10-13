from django.db import models
from django.core.validators import MaxValueValidator




# Patient Management Models

class Patient(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	DOB = models.DateField()
	SSN = models.IntegerField(primary_key= True, validators=[MaxValueValidator(999999999)],unique=True)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=2)
	zipcode =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")

class Request (models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	request_id = models.IntegerField(primary_key= True, validators=[MaxValueValidator(999999999)], unique=True)
	patient_id = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)
	doctor_id = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)
	description = models.CharField(max_length=1000)
	request_date = models.DateField()

	def __str__(self):
		return(f"{self.request_id}")

class Medical History(models.model):
	created_at = models.DateTimeField(auto_now_add=True)
	patient_id = models.IntegerField(primary_key= True, validators=[MaxValueValidator(999999999)], unique=True)
	illness_id = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)

	def __str__(self):
		return(f"{self.patient_id}")

class Illness(models.model):
	created_at = models.DateTimeField(auto_now_add=True)
	illness_id =  models.IntegerField(primary_key= True, validators=[MaxValueValidator(999999999)], unique=True)
	common_name = models.CharField(max_length=100)

	def __str__(self):
		return(f"{self.illness_id}")
		

# Create list of applicable doctor specialtys.
realSpecialty = [
	("General","General"),
	("Pediatrics","Pediatrics"),
	("Dermatology", "Dermatology"),
	("Surgery", "Surgery"),
	("Oncology", "Oncology"),
]

class Doctor(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	DOB = models.DateField()
	specialty = models.CharField(max_length=100, choices=realSpecialty)

	def __str__(self):
		return(f"{self.first_name} {self.last_name} {self.specialty}")



# In-Patient Management Models





# Medical Staff Management Models