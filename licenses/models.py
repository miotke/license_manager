from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class License(models.Model):

    # User input data
    date_of_entry = models.DateTimeField(default=timezone.now) # change this to be a date picker.
    software_name = models.CharField(max_length=100)
    license_key = models.CharField(max_length=100)
    purchase_date = models.CharField(max_length=8) # change this to a date picker.
    renewal_date = models.CharField(max_length=8, blank=True) # change this to be optional with a date picker.
    license_assigned_to = models.CharField(max_length=50)


    def save(self):
        super().save()


    def __str__(self):
        return self.software_name


    def get_absolute_url(self):
        return reverse('license-index')
