from django.contrib import admin
from .models import Software
from .models import License


# Register your models here.
admin.site.register(Software)
admin.site.register(License)