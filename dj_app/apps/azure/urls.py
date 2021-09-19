from django.urls import path
from .views import azure_api


urlpatterns = [
    path("", azure_api),
]
