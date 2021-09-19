import json
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

from apps.chat.models import Message
from azure.servicebus import ServiceBusMessage, ServiceBusClient


@receiver(post_save, sender=Message)
def send_message_to_slack(created, instance, *args, **kwargs):
    if created:
        if not instance.send_by_user:
            return
        sb_msg = {
            "source_thread_id": str(instance.thread.id),
            "body": instance.body,
            "info": instance.user,
            "source_type": "support"
        }
        msg = ServiceBusMessage(
            body=json.dumps(sb_msg),
            label="support"
        )
        client = ServiceBusClient.from_connection_string(settings.AZ_SB_CONN_STR)
        with client as client:
            with client.get_queue_sender(queue_name="content_inbound") as sender:
                sender.send_messages(msg)
