"""
This command creates a Software entry with a
randomly generated license key. By using this script
you will generate a software title and license key pair.
All pairs created with this script will show in the web
apps front-end and in the admin console.

The random word is generated from the system's
dictionary, assuming you're using a unix based system.

USAGE: `python manage.py create_software_title x`
where x = the number of software titles you want to create.

"""
import random
from licenses.models import License
from licenses.models import Software
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.utils import timezone


class Command(BaseCommand):

    help = "Auto generates a fake software title and a fake license key pair"


    def add_arguments(self, parser):
        parser.add_argument("total", type=int, help="Indicate how many fake software titles and license key pairs should be created.")


    def handle(self, *args, **kwargs):
        total = kwargs["total"]
        word_file = "/usr/share/dict/words"
        WORDS = open(word_file).read().splitlines()

        for i in range(total):

            for s in range(1):
                random_word = ''.join(WORDS[random.randint(1, len(WORDS))])

            software_title = Software(software_name=random_word)
            software_license_pair = License(associated_software=software_title,
                        license_key=get_random_string(),
                        license_assigned_by="Robot")

            software_title.save()
            software_license_pair.save()

            self.stdout.write(f"Created {software_license_pair}")
