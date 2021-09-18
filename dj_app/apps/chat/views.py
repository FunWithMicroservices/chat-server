from rest_framework.generics import CreateAPIView, RetrieveAPIView

from .models import Thread, Message
from .serializers import ThreadSerializer, PostMessageSerializer


class CreateThread(CreateAPIView):
    queryset = Thread.objects
    serializer_class = ThreadSerializer

    def perform_create(self, serializer):
        return serializer.save()


class RetrieveThread(RetrieveAPIView):
    queryset = Thread.objects
    serializer_class = ThreadSerializer


class CreateMessage(CreateAPIView):
    queryset = Message.objects
    serializer_class = PostMessageSerializer

    def perform_create(self, serializer):
        return serializer.save()


create_thread = CreateThread.as_view()
retrieve_thread = RetrieveThread.as_view()
create_message = CreateMessage.as_view()
