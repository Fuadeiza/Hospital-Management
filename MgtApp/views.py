from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView, TemplateView
from MgtApp.models import Patients
from MgtApp.forms import PatientsForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth
from django.contrib import messages

# Create your views here.


class index(TemplateView):
    template_name = "index.html"


class PatientsListView(LoginRequiredMixin,ListView):
    model = Patients
    template_name = "patients_list.html"

class PatientsCreateView(CreateView):
    form_class = PatientsForm
    model = Patients

class PatientsDetailView(LoginRequiredMixin,DetailView):
    login_url='/login/'
    redirect_field_name ='patients_detail.html'
    model = Patients
    slug_field = 'id'

