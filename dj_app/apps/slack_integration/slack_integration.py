from .models import SlackThread
import json
from django.conf import settings
from slack_sdk.web import WebClient
from apps.chat.models import Message


def get_slack_thread(thread):
    try:
        return SlackThread.objects.get(source_thread=thread)
    except SlackThread.DoesNotExist:
        return None


def send_to_slack(instance: Message, thread: SlackThread):
    client = WebClient(token=settings.SLACK_BOT_TOKEN)

    blocks = []

    if not thread:
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Hey there. *New Support Request received!*"
            }
        })
        json_info = json.dumps(instance.user, indent=True)
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*User Info*\n```{json_info}```"
            }
        })
        blocks.append({"type": "divider"})

    blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*Message*\n{instance.body}"
            }
        })

    response = client.chat_postMessage(
        channel=settings.SLACK_SUPPORT_CHANNEL,
        text="",
        blocks=blocks,
        thread_ts=None if not thread else thread.thread_ts,
    )

    if thread is None:
        SlackThread.objects.create(
            source_thread=instance.thread,
            source_type="support",
            info=instance.user,
            channel=settings.SLACK_SUPPORT_CHANNEL,
            thread_ts=response.data["ts"]
        )


def lead_message_to_slack(instance):
    slack_thread = get_slack_thread(instance.thread)
    send_to_slack(instance=instance, thread=slack_thread)
