from django.urls import path
from django.urls.conf import include
from django.conf import settings


urlpatterns = [
    path("chat/", include("apps.chat.urls")),
]

if "apps.slack_integration" in settings.INSTALLED_APPS:
    urlpatterns += [path("slack/", include("apps.slack_integration.urls"))]

if "apps.azure" in settings.INSTALLED_APPS:
    urlpatterns += [path("azure/", include("apps.azure.urls"))]
