from django import forms
from django.db import models
from MgtApp.models import Patients

class PatientsForm(forms.ModelForm):
    class Meta():
        model = Patients 
        exclude= ['user']