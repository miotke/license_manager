from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views
from .views import ListLicenseKeysView
from .views import ListSoftware

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"software", ListSoftware)


urlpatterns = [
    path("api/", include(router.urls))
]
