from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q


# Create your models here.
class License(models.Model):

    # User input data
    date_of_entry = models.DateTimeField(default=timezone.now)
    software_name = models.CharField(max_length=100)
    license_key = models.CharField(max_length=100)
    license_assigned_to = models.CharField(max_length=50, blank=True, default="License is free")
    purchase_date = models.DateField(default=timezone.now)
    renewal_date = models.DateField(default=timezone.now, blank=True)

    """
    TODO: Impliment this later.
    license_assigned_by should be a list populated by anyone
    within a specifc admin group or a superuser.

    For now it's just a required text field.
    """
    license_assigned_by = models.CharField(max_length=256)


    def save(self):
        super().save()


    def __str__(self):
        return self.software_name


    def get_absolute_url(self):
        return reverse("")
