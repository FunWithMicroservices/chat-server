from rest_framework import serializers

from .models import Thread, Message


class ThreadMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "user", "timestamp", "body", )


class ThreadSerializer(serializers.ModelSerializer):
    messages = ThreadMessageSerializer(many=True, read_only=True)

    class Meta:
        model = Thread
        fields = ('id', 'user', 'timestamp', 'messages', )


class PostMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
