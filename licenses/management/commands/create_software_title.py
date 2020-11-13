from licenses.models import Software
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.utils import timezone


class Command(BaseCommand):
    help = "Auto generates software titles to make life easier during testing"


    def add_arguments(self, parser):
        parser.add_argument("total", type=int, help="Indicates the number of software titles to create")


    def handle(self, *args, **kwargs):
        total = kwargs["total"]

        for i in range(total):
            software_title = Software(software_name=get_random_string())
            software_title.save()

            self.stdout.write(f"Created {software_title}")
