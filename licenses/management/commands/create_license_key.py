from licenses.models import License
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.utils import timezone


class Command(BaseCommand):
    help = "Auto generates fake license keys to make life easier during testing and development"


    def add_arguments(self, parser):
        parser.add_argument("total", type=int, help="Indicates the number of fake license keys to create")


    def handle(self, *args, **kwargs):
        total = kwargs["total"]

        for i in range(total):
            license_key = License(license_key=get_random_string())
            license_key.save()

            self.stdout.write(f"Created license key {license_key} for software ")