# tutorail/urls.py
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^doctor/$', views.Doctor, name='doctor'),
    url(r'^nurse/$', views.Nurse, name='nurse'),
    url(r'^medical_administrator/$', views.Medical_Administrator, name='medical_administrator'),
    url(r'^insurance_administrator/$', views.Insurance_Administrator, name='insurance_administrator'),
    url(r'^patient/$', views.Patient, name='patient'),
    url(r'^record/$', views.Record, name='record'),
    url(r'^doctor_exam_record/$', views.Doctor_Exam_Record, name='doctor_exam_record'),
    url(r'^diagnosis_record/$', views.Diagnosis_Record, name='diagnosis_record'),
    url(r'^test_results_record/$', views.Test_Results_Record, name='test_results_record'),
    url(r'^insurance_claim_record/$', views.Insurance_Claim_Record, name='insurance_claim_record'),
    url(r'^patient_doctor_correspondence_record/$', views.Patient_Doctor_Correspondence_Record, name='patient_doctor_correspondence_record'),
    url(r'^raw_record/$', views.Raw_Record, name='raw_record'),
    url(r'^note/$', views.Note, name='note'),
    ]

