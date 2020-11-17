"""
This command creates a Software entry without
a license key. Since there is not an associated license
key the software titles generated with this script
will not appear in the web apps front-end but will show
under Software in the admin console.

If you need generate a Software and License pair
refer to create_software_license_pairs.py in the
same directory as this script.

USAGE: `python manage.py create_software_title x`
where x = the number of software titles you want to create.

"""

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
