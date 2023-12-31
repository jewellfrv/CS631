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

class Request (models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	request_id = models.IntegerField(primary_key= True, validators=[MaxValueValidator(999999999)], unique=True)
	patient_id = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)
	emploment_number = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)
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
		

class Illness(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	common_name = models.CharField(max_length=100)

	def __str__(self):
		return(f"{self.id}")
      

class MedicalHistory(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	illness = models.ForeignKey(Illness, on_delete=models.CASCADE)

	def __str__(self):
		return(f"Patient {self.patient} with {self.illness}")
      

class Request(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    physician = models.ForeignKey(Physician, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=1000)
    treatment_type = models.CharField(max_length=20, choices=[("General", "General"),
                                                              ("Surgery", "Surgery")], default='General')
    request_date = models.DateField()
    def __str__(self):
        return(f"{self.id}")
    
    def save(self, *args, **kwargs):
        today = date.today()
        if self.request_date <= today:
            self.description = "Not Valid"

        # Save the InPatient object
        super(Request, self).save(*args, **kwargs)

class Medication (models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	medication_id = models.IntegerField(primary_key= True, validators=[MaxValueValidator(999999999)], unique=True)
	patient_id = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)
	quantity_on_hand = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)
	quantity_on_order = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)
	unit_cost = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)
	YTD_usage = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)
	physician = models.ForeignKey(Physician, on_delete=models.SET_NULL, null=True, blank=True)
	description = models.CharField(max_length=1000)
	name = models.CharField(max_length=100)
	severity = models.CharField(max_length=100)
	prescription_date = models.DateField()

	def __str__(self):
		return(f"{self.medication_id}")


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
    
    def update_occupation_status(self):
        # Check if the bed is occupied in any InPatient record
        is_occupied = InPatient.objects.filter(bed=self, discharge_date__gte=date.today()).exists()

        # Update the is_occupied field
        self.is_occupied = is_occupied
        self.save()
        

class InPatient(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    admission_date = models.DateField()
    discharge_date = models.DateField(null=True, blank=True)
    physician = models.ForeignKey(Physician, on_delete=models.SET_NULL, null=True, blank=True)
    nurse = models.ForeignKey(Nurse, on_delete=models.SET_NULL,null=True,blank=True)
    treatment_type = models.CharField(max_length=20, choices=[("General", "General"),
                                                              ("Surgery", "Surgery")], default='General')

 


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

class Physician(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	DOB = models.DateField()
	gender =  models.CharField(max_length=50)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=2)
	zipcode =  models.CharField(max_length=20)
	SSN = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)
	employment_number = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)

	specialty = models.CharField(max_length=100, choices=realSpecialty)

	def __str__(self):
		return(f"Dr.{self.first_name} {self.last_name}/ Specialty: {self.specialty} / ID: {self.id} ")

class Nurse(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	DOB = models.DateField()
	gender =  models.CharField(max_length=50)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=2)
	zipcode =  models.CharField(max_length=20)
	SSN = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)
	employment_number = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)

	specialty = models.CharField(max_length=100, choices=realSpecialty)

	def __str__(self):
		return(f"Nurse {self.first_name} {self.last_name} / ID: {self.id} ")


class Surgeon(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	DOB = models.DateField()
	gender =  models.CharField(max_length=50)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=2)
	zipcode =  models.CharField(max_length=20)
	Contract =  models.CharField(max_length=50)
	SSN = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)
	specialty = models.CharField(max_length=100, choices=realSpecialty)
	employment_number = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)

	specialty = models.CharField(max_length=100, choices=realSpecialty)

	def __str__(self):
		return(f"Surgeon.{self.first_name} {self.last_name}/ Specialty: {self.specialty} / ID: {self.id} ")


class Receptionist(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	DOB = models.DateField()
	gender =  models.CharField(max_length=50)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=2)
	zipcode =  models.CharField(max_length=20)
	SSN = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)
	employment_number = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)

	def __str__(self):
		return(f"Receptionist {self.first_name} {self.last_name} / ID: {self.id} ")


class Administrative_Associate (models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	DOB = models.DateField()
	gender =  models.CharField(max_length=50)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=2)
	zipcode =  models.CharField(max_length=20)
	SSN = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)
	employment_number = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)

	def __str__(self):
		return(f"Administrative_Associate {self.first_name} {self.last_name} / ID: {self.id} ")


class Salary (models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	Type =  models.CharField(max_length=50)
	position = models.CharField(max_length=50
	amount = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)
	employment_number = models.IntegerField (validators=[MaxValueValidator (999999999)], unique=True)

	def __str__(self):
		return(f"Salary {self.first_name} {self.last_name} / ID: {self.id} ")


# Create list of applicable Physician specialtys.

realSpecialty = [
	("General","General"),
	("Pediatrics","Pediatrics"),
	("Gynocology", "Gynocology"),
	("Opthamology", "Opthamology"),
	("Oncology", "Oncology"),
]	