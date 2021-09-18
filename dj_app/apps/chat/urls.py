from django.urls import path
from .views import create_thread, retrieve_thread, create_message


urlpatterns = [
    path("thread/", create_thread),
    path("thread/<pk>/", retrieve_thread),
    path("message/", create_message),
]
