from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import Software
from .models import License


class ListLicenseKeysView(LoginRequiredMixin, ListView):

    model = License
    template_name = "templates/index.html"
    context_object_name = "licenses"
    ordering = ["associated_software"]