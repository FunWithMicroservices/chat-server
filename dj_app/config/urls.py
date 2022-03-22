from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("api/", include("apps.urls")),
    path("monitoring/", include("django_prometheus.urls")),
]
