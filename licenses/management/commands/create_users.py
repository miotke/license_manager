"""
This was a simple management command to get familiar
with Django management commands again, it's be a while.

USAGE: `python manage.py create_users x`
where x = the number of users you want to create.

"""


from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = "Create random users"


    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Indicates the number users to be created")


    def handle(self, *args, **kwargs):
        name = kwargs["name"]
        password = get_random_string()

        User.objects.create_user(username=name, email="", password=password)

        self.stdout.write(f"Account created \n 🙋‍♂️Username: {name} \n 🔐 Password: {password} \n")

        parser.add_argument("total", type=int, help="Indicates the number users to be created")
