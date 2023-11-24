from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Patient, Physician, Surgeon, Medication, realSpecialty, Nurse, Room, Bed, InPatient, Request

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	




# Create Add Patient Form
class AddPatientForm(forms.ModelForm):
	first_name = forms.CharField(required=True, 
							  widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), 
							  label="")
	last_name = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), 
							 label="")
	DOB = forms.DateField(required=True, 
					   widget=forms.widgets.DateInput(attrs={"placeholder":"Date of Birth", "class":"form-control"}),
					   label="Year-Month-Day")
	SSN = forms.IntegerField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"SSN", "class":"form-control"}), 
						 label="")	
	email = forms.CharField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), 
						 label="")
	phone = forms.CharField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), 
						 label="")
	address = forms.CharField(required=True, 
						   widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), 
						   label="")
	city = forms.CharField(required=True, 
						widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), 
						label="")
	state = forms.CharField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}),
						   label="")
	zipcode = forms.CharField(required=True, 
						   widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), 
						   label="")

	class Meta:
		model = Patient
		exclude = ("user",)
		

# Create Add Physician Form
class AddPhysicianForm(forms.ModelForm):
	first_name = forms.CharField(required=True, 
							  widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), 
							  label="")
	last_name = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), 
							 label="")
	gender = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Gender", "class":"form-control"}), 
							 label="")
	phone = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), 
							 label="")
	address = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), 
							 label="")
	city = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), 
							 label="")
	state = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), 
							 label="")
	zipcode = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), 
							 label="")						 						 						 						 						 						 
	DOB = forms.DateField(required=True, 
					   widget=forms.widgets.DateInput(attrs={"placeholder":"Date of Birth", "class":"form-control"}),
					   label="Year-Month-Day")
	SSN = forms.IntegerField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"SSN", "class":"form-control"}), 
						 label="")
	employment_number = forms.IntegerField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"Employment Number", "class":"form-control"}), 
						 label="")						 					   	
	specialty = forms.ChoiceField(required=True, 
							 choices=realSpecialty,
                             widget=forms.Select(attrs={"placeholder":"Specialty", "class":"form-control"}), 
							 label="")
	class Meta:
		model = Physician
		exclude = ("user",)



# Create Add Surgeon Form
class AddSurgeonForm(forms.ModelForm):
	first_name = forms.CharField(required=True, 
							  widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), 
							  label="")
	last_name = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), 
							 label="")
	gender = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Gender", "class":"form-control"}), 
							 label="")
	phone = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), 
							 label="")
	address = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), 
							 label="")
	city = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), 
							 label="")
	state = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), 
							 label="")
	zipcode = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), 
							 label="")
	contract = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Contract", "class":"form-control"}), 
							 label="")						 						 						 						 						 						 						 
	DOB = forms.DateField(required=True, 
					   widget=forms.widgets.DateInput(attrs={"placeholder":"Date of Birth", "class":"form-control"}),
					   label="Year-Month-Day")
	SSN = forms.IntegerField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"SSN", "class":"form-control"}), 
						 label="")
	employment_number = forms.IntegerField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"Employment Number", "class":"form-control"}), 
						 label="")						 					   	
	specialty = forms.ChoiceField(required=True, 
							 choices=realSpecialty,
                             widget=forms.Select(attrs={"placeholder":"Specialty", "class":"form-control"}), 
							 label="")
	class Meta:
		model = Surgeon
		exclude = ("user",)



# Create Add Nurse Form
class AddNurseForm(forms.ModelForm):
	first_name = forms.CharField(required=True, 
							  widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), 
							  label="")
	last_name = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), 
							 label="")
	gender = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Gender", "class":"form-control"}), 
							 label="")
	phone = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), 
							 label="")
	address = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), 
							 label="")
	city = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), 
							 label="")
	state = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), 
							 label="")
	zipcode = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), 
							 label="")						 						 						 						 						 						 
	DOB = forms.DateField(required=True, 
					   widget=forms.widgets.DateInput(attrs={"placeholder":"Date of Birth", "class":"form-control"}),
					   label="Year-Month-Day")
	SSN = forms.IntegerField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"SSN", "class":"form-control"}), 
						 label="")
	employment_number = forms.IntegerField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"Employment Number", "class":"form-control"}), 
						 label="")						 					   	
	specialty = forms.ChoiceField(required=True, 
							 choices=realSpecialty,
                             widget=forms.Select(attrs={"placeholder":"Specialty", "class":"form-control"}), 
							 label="")
	class Meta:
		model = Nurse
		exclude = ("user",)


# Create Add Receptionist Form
class AddReceptionistForm(forms.ModelForm):
	first_name = forms.CharField(required=True, 
							  widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), 
							  label="")
	last_name = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), 
							 label="")
	gender = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Gender", "class":"form-control"}), 
							 label="")
	phone = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), 
							 label="")
	address = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), 
							 label="")
	city = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), 
							 label="")
	state = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), 
							 label="")
	zipcode = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), 
							 label="")						 						 						 						 						 						 
	DOB = forms.DateField(required=True, 
					   widget=forms.widgets.DateInput(attrs={"placeholder":"Date of Birth", "class":"form-control"}),
					   label="Year-Month-Day")
	SSN = forms.IntegerField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"SSN", "class":"form-control"}), 
						 label="")
	employment_number = forms.IntegerField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"Employment Number", "class":"form-control"}), 
						 label="")						 					   	
	
	
	class Meta:
		model = Receptionist
		exclude = ("user",)


# Create Add Administrative_Associate Form
class AddAdministrative_AssociateForm(forms.ModelForm):
	first_name = forms.CharField(required=True, 
							  widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), 
							  label="")
	last_name = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), 
							 label="")
	gender = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Gender", "class":"form-control"}), 
							 label="")
	phone = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), 
							 label="")
	address = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), 
							 label="")
	city = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), 
							 label="")
	state = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), 
							 label="")
	zipcode = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), 
							 label="")						 						 						 						 						 						 
	DOB = forms.DateField(required=True, 
					   widget=forms.widgets.DateInput(attrs={"placeholder":"Date of Birth", "class":"form-control"}),
					   label="Year-Month-Day")
	SSN = forms.IntegerField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"SSN", "class":"form-control"}), 
						 label="")
	employment_number = forms.IntegerField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"Employment Number", "class":"form-control"}), 
						 label="")						 					   	
	specialty = forms.ChoiceField(required=True, 
							 choices=realSpecialty,
                             widget=forms.Select(attrs={"placeholder":"Specialty", "class":"form-control"}), 
							 label="")
	class Meta:
		model = Administrative_Associate
		exclude = ("user",)




# Create Add Request Form
class AddRequestForm(forms.ModelForm):
    
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(), required=True,
        widget=forms.widgets.Select(attrs={"placeholder": "Patient", "class": "form-control"}),
        label="Patient"
    )
    physician = forms.ModelChoiceField(
    queryset=Physician.objects.all(),
    required=True,
    widget=forms.widgets.Select(attrs={"placeholder": "Physician", "class": "form-control"}),
    label="Physician",
    to_field_name="id"  # This specifies which field to use as the value
	)

    treatment_type = forms.ChoiceField(
        choices=[('General', 'General'), ('Surgery', 'Surgery')],
        required=True,
        widget=forms.widgets.Select(attrs={"placeholder": "Treatment Type", "class": "form-control"}),
        label="Treatment Type"
    )
    description = forms.CharField(required=True, 
							 widget=forms.widgets.TextInput(attrs={"placeholder":"Description", "class":"form-control"}), 
							 label="")
    
    request_date = forms.DateField(required=True, 
					   widget=forms.widgets.DateInput(attrs={"placeholder":"Request Date", "class":"form-control"}),
					   label="Year-Month-Day")
    class Meta:
        model = Request
        exclude = ("user",)
        fields = ['patient', 'doctor', 'treatment_type', 'description','request_date']


# Create Add Medication Form
class AddMedicationForm(forms.ModelForm):
	
	medication_id = forms.IntegerField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"Medication ID", "class":"form-control"}), 
						 label="")	
	patient_id = forms.IntegerField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"Patient ID", "class":"form-control"}), 
						 label="")		
	quantity_on_hand = forms.IntegerField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"Quantity on Hand", "class":"form-control"}), 
						 label="")	
	quantity_on_order = forms.IntegerField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"Quantity on Order", "class":"form-control"}), 
						 label="")	
	unit_cost = forms.IntegerField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"Unit Cost", "class":"form-control"}), 
						 label="")
	YTD_usage = forms.IntegerField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"YTD Usage", "class":"form-control"}), 
						 label="")						 						 					 					 				 
	physician = forms.CharField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"Physician", "class":"form-control"}), 
						 label="")
	description = forms.CharField(required=True, 
						 widget=forms.widgets.TextInput(attrs={"placeholder":"Description", "class":"form-control"}), 
						 label="")
	name = forms.CharField(required=True, 
						   widget=forms.widgets.TextInput(attrs={"placeholder":"Name", "class":"form-control"}), 
						   label="")
	severity = forms.CharField(required=True, 
						widget=forms.widgets.TextInput(attrs={"placeholder":"Severity", "class":"form-control"}), 
						label="")
	prescription_date = forms.DateField(
        required=False,
        widget=forms.widgets.DateInput(attrs={"placeholder": "Prescription Date", "class": "form-control"}),
        label="Prescription Date"
    )					
	
	class Meta:
		model = Medication
		exclude = ("user",)



# Create Add Medical History Form
class AddMedicalHistoryForm(forms.ModelForm):
	SSN = forms.IntegerField(required=True, 
							  widget=forms.widgets.TextInput(attrs={"placeholder":"SSN", "class":"form-control"}), 
							  label="")
	illness_id = forms.IntegerField(required=True, 
							  widget=forms.widgets.TextInput(attrs={"placeholder":"Illness ID", "class":"form-control"}), 
							  label="")


	class Meta:
		model = MedicalHistory
		exclude = ("user",)





# Create Add Room Form
class RoomForm(forms.ModelForm):
    room_number = forms.CharField(required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Room Number", "class": "form-control"}),
        label="Room Number"
    )
    floor = forms.IntegerField(required=True,
        widget=forms.widgets.NumberInput(attrs={"placeholder": "Floor", "class": "form-control"}),
        label="Floor"
    )
    wing = forms.CharField(required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Wing", "class": "form-control"}),
        label="Wing"
    )
    description = forms.CharField(
        widget=forms.widgets.Textarea(attrs={"placeholder": "Description", "class": "form-control"}),
        label="Description",
        required=False  
    )

    class Meta:
        model = Room
        fields = ['room_number', 'floor', 'wing', 'description']

# Create Add Bed Form
class BedForm(forms.ModelForm):
    room = forms.ModelChoiceField(queryset=Room.objects.all(), required=True,
        widget=forms.widgets.Select(attrs={"placeholder": "Room", "class": "form-control"}),
        label="Room"
    )
    bed_number = forms.IntegerField(required=True,
        widget=forms.widgets.NumberInput(attrs={"placeholder": "Bed Number", "class": "form-control"}),
        label="Bed Number"
    )
    is_occupied = forms.BooleanField(
        required=False,
        widget=forms.widgets.CheckboxInput(attrs={"class": "form-check-input"}),
        label="Is Occupied"
    )

    class Meta:
        model = Bed
        fields = ['room', 'bed_number', 'is_occupied']


# Create Add InPatient Form
class AddInPatientForm(forms.ModelForm):
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(), required=True,
        widget=forms.widgets.Select(attrs={"placeholder": "Patient", "class": "form-control"}),
        label="Patient"
    )
    bed = forms.ModelChoiceField(queryset=Bed.objects.filter(is_occupied=False), required=True,
        widget=forms.widgets.Select(attrs={"placeholder": "Bed", "class": "form-control"}),
        label="Bed"
    )
    admission_date = forms.DateField(required=True,
        widget=forms.widgets.DateInput(attrs={"placeholder": "Admission Date", "class": "form-control"}),
        label="Admission Date"
    )
    discharge_date = forms.DateField(
        required=False,
        widget=forms.widgets.DateInput(attrs={"placeholder": "Discharge Date", "class": "form-control"}),
        label="Discharge Date"
    )
    
    physician = forms.ModelChoiceField(
    queryset=Physician.objects.all(),
    required=True,
    widget=forms.widgets.Select(attrs={"placeholder": "Physician", "class": "form-control"}),
    label="Physician",
    to_field_name="id"  # This specifies which field to use as the value
	)
    nurse = forms.ModelChoiceField(
	queryset=Nurse.objects.all(),
	required=True,
	widget=forms.widgets.Select(attrs={"placeholder": "Nurse", "class": "form-control"}),
	label="Nurse",
	to_field_name="id"  
	)
    treatment_type = forms.ChoiceField(
        choices=[('General', 'General'), ('Surgery', 'Surgery')],
        required=True,
        widget=forms.widgets.Select(attrs={"placeholder": "Treatment Type", "class": "form-control"}),
        label="Treatment Type"
    )

    def __init__(self, *args, **kwargs):
        super(AddInPatientForm, self).__init__(*args, **kwargs)

    class Meta:
        model = InPatient
        fields = ['patient', 'bed', 'admission_date', 'discharge_date', 'physician', 'nurse', 'treatment_type']
