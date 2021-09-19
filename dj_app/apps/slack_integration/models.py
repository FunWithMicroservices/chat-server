from django.db import models
from apps.chat.models import Thread


class SlackThread(models.Model):
    source_thread = models.OneToOneField(
        to=Thread,
        primary_key=True,
        on_delete=models.CASCADE
    )
    thread_ts = models.CharField(
        max_length=30,
        db_index=True
    )
    source_type = models.CharField(
        max_length=20
    )
    info = models.JSONField()
    channel = models.CharField(max_length=40)


class SlackResponseMessage(models.Model):
    slack_thread = models.ForeignKey(
        to=SlackThread,
        on_delete=models.CASCADE
    )
    body = models.TextField()
