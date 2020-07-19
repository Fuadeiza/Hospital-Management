from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Value
from django.db.models.functions import Concat


# Create your models here.
class Patients(models.Model):
    #additional objects 
    name=models.CharField(max_length=120, null=True)
    email=models.EmailField(max_length=120,null=True)
    diagnosis= models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    date_of_consultation= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('MgtApp:list')