# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import System_Administrator, Doctor, Nurse, Medical_Administrator, Insurance_Administrator, Patient, Record, Doctor_Exam_Record, Diagnosis_Record, Test_Results_Record, Insurance_Claim_Record, Patient_Doctor_Correspondence_Record, Raw_Record, Note

# Register your models here.
admin.site.register(System_Administrator)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Medical_Administrator)
admin.site.register(Insurance_Administrator)
admin.site.register(Patient)
admin.site.register(Record)
admin.site.register(Doctor_Exam_Record)
admin.site.register(Diagnosis_Record)
admin.site.register(Test_Results_Record)
admin.site.register(Insurance_Claim_Record)
admin.site.register(Patient_Doctor_Correspondence_Record)
admin.site.register(Raw_Record)
admin.site.register(Note)

