from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("chat/", include("apps.chat.urls")),
    path("slack/", include("apps.slack_integration.urls")),
]
