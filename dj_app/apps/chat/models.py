import uuid
from django.db import models


class Thread(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid1
    )
    user = models.JSONField()
    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.id


class Message(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid1
    )
    thread = models.ForeignKey(
        to=Thread,
        on_delete=models.CASCADE,
        related_name="messages"
    )
    user = models.JSONField()
    timestamp = models.DateTimeField(
        auto_now_add=True
    )
    body = models.TextField()
    send_by_user = models.BooleanField(
        default=True,
        help_text="If False the message was sent from Slack"
    )

    class Meta:
        ordering = ('-timestamp', )

    def __str__(self):
        return f"Msg for Thread {self.thread.id}"
