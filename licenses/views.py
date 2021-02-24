from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string # We may not need this import
from django.http import HttpResponse
from django.http import HttpResponseRedirect
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


    def search_product(request): 
        # Search function
        if request.method == "POST": 
            query_name = request.POST.get("software_name", None)
            
            if query_name:
                results = Software.objects.filter(name__contains=query_name)
                return render(request, "product-search.html", {"results": results})

            return render(request, "product-search.html")
