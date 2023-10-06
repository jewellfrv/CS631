from django.db import models


class Patient(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	DOB = models.DateField()
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
	

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