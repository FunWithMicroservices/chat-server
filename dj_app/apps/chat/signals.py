from django.dispatch import receiver
from django.db.models.signals import post_save
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from .models import Message
from .serializers import ThreadMessageSerializer


@receiver(post_save, sender=Message)
def send_message_to_socket(created, instance, *args, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        serializer = ThreadMessageSerializer(instance)
        async_to_sync(channel_layer.group_send)(
            f"thread_{instance.thread.id}", {
                'type': 'send_message',
                'context': serializer.data
            }
        )
