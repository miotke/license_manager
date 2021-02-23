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


    def search_page(request):
        # Get search_term from template
        search_key = request.POST.get("search_term")
        request.session["search_key"] = search_key

        # Redirect to search results page
        return HttpResponseRedirect("/item/search-results")


    # Return the search results page
    def search_results(request):
        search_key = request.session["search_key"]

        # Query results text that contains what you typed in
        results = Software.object.filter(text__contains=search_key)

        context = {
            "search_term": search_key,
            "results": results
        }

        return render(request, "templates/search_results.html", context)
