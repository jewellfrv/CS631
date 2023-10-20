from django.db import models
from django.core.validators import MaxValueValidator
from datetime import date




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
     

class Illness(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	common_name = models.CharField(max_length=100)

	def __str__(self):
		return(f"{self.id}")
      

class MedicalHistory(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	SSN = models.ForeignKey(Patient, on_delete=models.CASCADE)
	illness_id = models.ForeignKey(Illness, on_delete=models.CASCADE)

	def __str__(self):
		return(f"Patient {self.SSN} with ")
      

class Request(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	request_id = models.IntegerField(primary_key= True)
	SSN = models.ForeignKey(Patient, on_delete=models.CASCADE)
	doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	description = models.CharField(max_length=1000)
	request_date = models.DateField()

	def __str__(self):
		return(f"{self.request_id}")




# In-Patient Management Models

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    floor = models.PositiveIntegerField()
    wing = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Room {self.room_number}, Floor {self.floor}"

class Bed(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    bed_number = models.PositiveIntegerField()
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"Bed {self.bed_number} in {self.room}"

    class Meta:
        unique_together = ('room', 'bed_number')

class InPatient(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    admission_date = models.DateField()
    discharge_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"In-Patient: {self.patient} in Bed {self.bed}"

    def save(self, *args, **kwargs):
        today = date.today()
        if self.discharge_date and self.discharge_date <= today:
            self.bed.is_occupied = False
        else:
            self.bed.is_occupied = True
        self.bed.save()

        # Save the InPatient object
        super(InPatient, self).save(*args, **kwargs)


# Medical Staff Management Models