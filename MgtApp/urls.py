from django.urls import path, include
from MgtApp import views
from MgtApp.views import index , PatientsListView, PatientsDetailView, PatientsCreateView

app_name= 'MgtApp'

urlpatterns = [
    path('list', PatientsListView.as_view(), name='list'),
    path('<slug:slug>/', PatientsDetailView.as_view(), name='detail'),
    path('create', PatientsCreateView.as_view(), name='create'),
]