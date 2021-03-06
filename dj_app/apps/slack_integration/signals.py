from django.dispatch import receiver
from django.db.models.signals import post_save

import logging

from apps.chat.models import Message
from .slack_integration import lead_message_to_slack

from langdetect import detect


logger = logging.getLogger(__name__)

@receiver(post_save, sender=Message)
def send_message_to_slack(created, instance, *args, **kwargs):
    if created:
        if not instance.send_by_user:
            return
        if detect(instance.body) != 'en':
            logger.info(f"THROW AWAY THAT SHT {instance.body}")
            return
        logger.info(f"SEND MSG {instance.body}")
        lead_message_to_slack(instance)
