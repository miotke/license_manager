from rest_framework import serializers
from .models import Software

class SoftwareSerializer(serializers.ModelSerializer): 
    class Meta: 
        fields = ("id", "software_name", "date_of_entry", "purchase_date")
        model = Software
