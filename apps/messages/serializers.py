from rest_framework import serializers

from apps.messages.models import SendMessagesModel


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendMessagesModel
        fields = '_all_'
