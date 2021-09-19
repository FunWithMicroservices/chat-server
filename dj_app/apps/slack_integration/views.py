from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from apps.chat.models import Message
from .models import SlackThread


class SlackAPI(CreateAPIView):
    def post(self, request, *args, **kwargs):
        if request.data["type"] == "url_verification":
            return Response({"challenge": request.data["challenge"]})

        event_id = request.data["event_id"]
        event = request.data["event"]
        if event["type"] != "message":
            return Response({"challenge": event_id})

        if "thread_ts" not in event:
            return Response({"challenge": event_id})

        try:
            thread = SlackThread.objects.get(thread_ts=event["thread_ts"])
        except SlackThread.DoesNotExist:
            return Response({"challenge": event_id})

        if not event["text"].startswith("*send* "):
            return Response({"challenge": event_id})

        Message.objects.create(
            thread=thread.source_thread,
            user={"username": "slack"},
            body=event["text"].lstrip("*send* "),
            send_by_user=False
        )

        return Response({"challenge": event_id})


slack_api = SlackAPI.as_view()
