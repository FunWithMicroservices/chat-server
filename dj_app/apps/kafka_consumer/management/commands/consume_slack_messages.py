import logging
import json

from django.conf import settings
from django.core.management.base import BaseCommand

from confluent_kafka import Consumer
from apps.chat.models import Message, Thread


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        logger.info(f"{settings.KAFKA_CONF}")
        consumer = Consumer(**settings.KAFKA_CONF)
        consumer.subscribe(["customer-platform-contact-form"])

        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                logger.info("No message received")
            elif msg.error():
                logger.info("An Error occurred")
            else:
                logger.info(f"Message received: {msg.value()}")
                try:
                    message_value = json.loads(msg.value().decode("utf-8"))
                    user = {
                        "name": message_value.get("name", "UNKNOWN"),
                        "topic": message_value.get("type", "UNKNOWN"),
                        "email": message_value.get("email", "UNKNOWN"),
                    }
                    thread = Thread.objects.create(user=user)
                    Message.objects.create(thread=thread, user=user, body=message_value["message"])
                except AssertionError:
                    continue
