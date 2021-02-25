from django.test import TestCase
from .models import Software
from django.utils import timezone


class SoftwareTest(TestCase):

    @classmethod
    def setupTestData(cls):
        Software.objects.create(software_name="Gus Photos")
        Software.objects.create(purchase_date=timezone.now)
        Software.objects.create(date_of_entry=timezone.now)

    
    def test_software_name(self): 
        software = Software.objects.get(id=1)
        expected_object_name = f"{software.software_name}"
        self.assertEquals(expected_object_name, "Gus Photos")
    
    def test_purchase_date(self):
        pass
