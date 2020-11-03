from django.urls import path
from .views import ListLicenseKeysView

urlpatterns = [
    path("", ListLicenseKeysView.as_view(), name="license-index"),
]
