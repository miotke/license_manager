from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q


class Software(models.Model):

    # User input data
    date_of_entry = models.DateTimeField(default=timezone.now)
    purchase_date = models.DateField(default=timezone.now)
    software_name = models.CharField(max_length=100)


    def save(self):
        super().save()


    def __str__(self):
        return self.software_name


    def get_absolute_url(self):
        return reverse("")


class License(models.Model):
    """
    The License model contains all information directly
    related to a specific license key. A License will
    have a many-to-one relationship with Software. This means
    that each license will be assigned to a piece of software.
    Each piece of software can have multiple licenses.
    """

    date_of_entry = models.DateField(default=timezone.now)
    license_key = models.CharField(max_length=256)
    """
    TODO: Impliment this later.
    license_assigned_by should be a list populated by anyone
    within a specifc admin group or a superuser.

    For now it's just a required text field.
    """
    license_assigned_to = models.CharField(max_length=50, blank=True, default="License is free")
    purchase_date = models.DateField(default=timezone.now)
    renewal_date = models.DateField(default=timezone.now)
    associated_software = models.ForeignKey(Software, on_delete=models.PROTECT)


    def save(self):
        super().save()


    def __str__(self):
        return self.license_assigned_to


    class Meta:
        ordering = ["associated_software"]
