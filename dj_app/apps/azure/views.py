from rest_framework.generics import CreateAPIView, get_object_or_404
from apps.chat.models import Thread, Message
from rest_framework.response import Response
from rest_framework import status


class AzureAPI(CreateAPIView):
    def post(self, request, *args, **kwargs):
        # No time for serializer lol
        # ANARCHIIIIIE

        thread = get_object_or_404(Thread, id=request.data["source_thread_id"])
        Message.objects.create(
            thread=thread,
            user={"username": "Support"},
            body=request.data["body"],
            send_by_user=False
        )

        return Response(status=status.HTTP_201_CREATED)


azure_api = AzureAPI.as_view()
