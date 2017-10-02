# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django import forms
from django.shortcuts import render, redirect
from django.utils import timezone
from app.forms import *

def Doctor(request):
    if request.method == "POST":
        form = Doctor_Form(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/admin')
    else:
        return render(request, "app/my_template.html", {'form': Doctor_Form()})
 
def Nurse(request):
    if request.method == "POST":
        form = Nurse_Form(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/admin')
    else:
        return render(request, "app/my_template.html", {'form': Nurse_Form()})
 
def Medical_Administrator(request):
    if request.method == "POST":
        form = Medical_Administrator_Form(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/admin')
    else:
        return render(request, "app/my_template.html", {'form': Medical_Administrator()})

def Insurance_Administrator(request):
    if request.method == "POST":
        form = Insurance_Administrator_Form(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/admin')
    else:
        return render(request, "app/my_template.html", {'form': Insurance_Administrator()})

def Patient(request):
    if request.method == "POST":
        form = Patient_Form(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/admin')
    else:
        return render(request, "app/my_template.html", {'form': Patient()})

def Record(request):
    if request.method == "POST":
        form = Record_Form(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/admin')
    else:
        return render(request, "app/my_template.html", {'form': Record()})

def Doctor_Exam_Record(request):
    if request.method == "POST":
        form = Doctor_Exam_Record_Form(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/admin')
    else:
        return render(request, "app/my_template.html", {'form': Doctor_Exam_Record()})

def Diagnosis_Record(request):
    if request.method == "POST":
        form = Diagnosis_Record_Form(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/admin')
    else:
        return render(request, "app/my_template.html", {'form': Diagnosis_Record()})

def Test_Results_Record(request):
    if request.method == "POST":
        form = Test_Results_Record_Form(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/admin')
    else:
        return render(request, "app/my_template.html", {'form': Test_Results_Record()})

def Insurance_Claim_Record(request):
    if request.method == "POST":
        form =Insurance_Claim_Record_Form(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/admin')
    else:
        return render(request, "app/my_template.html", {'form': Insurance_Claim_Record()})

def Patient_Doctor_Correspondence_Record(request):
    if request.method == "POST":
        form =Patient_Doctor_Correspondence_Record_Form(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/admin')
    else:
        return render(request, "app/my_template.html", {'form': Patient_Doctor_Correspondence_Record()})

def Raw_Record(request):
    if request.method == "POST":
        form =Raw_Record_Form(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/admin')
    else:
        return render(request, "app/my_template.html", {'form': Raw_Record()})

def Note(request):
    if request.method == "POST":
        form = Note_Form(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/admin')
    else:
        return render(request, "app/my_template.html", {'form': Note_Form()})
 


