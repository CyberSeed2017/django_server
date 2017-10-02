from django.forms import ModelForm
from app.models import System_Administrator, Doctor, Nurse, Medical_Administrator, Insurance_Administrator, Patient, Record, Doctor_Exam_Record, Diagnosis_Record, Test_Results_Record, Insurance_Claim_Record, Patient_Doctor_Correspondence_Record, Raw_Record, Note
 
class Doctor_Form(ModelForm):
    class Meta:
        model = Doctor
        fields = ['Practice_Name', 'Practice_Address', 'Recovery_Phrase']

class Nurse_Form(ModelForm):
    class Meta:
        model = Nurse
        fields = ['Practice_Name', 'Practice_Address', 'Associated_Doctors']

class Medical_Administrator_Form(ModelForm):
    class Meta:
        model = Medical_Administrator
        fields = ['Practice_Name', 'Practice_Address', 'Associated_Doctors', 'Associated_Nurses']

class Insurance_Administrator_Form(ModelForm):
    class Meta:
        model = Insurance_Administrator
        fields = ['Company_Name', 'Company_Address']

class Patient_Form(ModelForm):
    class Meta:
        model = Patient
        fields = ['SSN', 'Address', 'DOB']

class Record_Form(ModelForm):
    class Meta:
        model = Record
        fields = ['Record_Type', 'Patient']

class Doctor_Exam_Record_Form(ModelForm):
    class Meta:
        model = Doctor_Exam_Record
        fields = ['Notes']

class Diagnosis_Record_Form(ModelForm):
    class Meta:
        model = Diagnosis_Record
        fields = ['Doctor', 'Diagnosis']

class Test_Results_Record_Form(ModelForm):
    class Meta:
        model = Test_Results_Record
        fields = ['Lab', 'Notes', 'Record']

class Insurance_Claim_Record_Form(ModelForm):
    class Meta:
        model = Insurance_Claim_Record
        fields = ['Amount', 'Status']

class Patient_Doctor_Correspondence_Record_Form(ModelForm):
    class Meta:
        model = Patient_Doctor_Correspondence_Record
        fields = ['Doctor', 'Notes']

class Raw_Record_Form(ModelForm):
    class Meta:
        model = Raw_Record
        fields = ['File', 'Description']

class Note_Form(ModelForm):
    class Meta:
        model = Note
        fields = ['Text', 'Patient_Doctor_Correspondence']

