from rest_framework.generics import CreateAPIView

from apps.messages.models import SendMessagesModel
from apps.messages.serializers import MessageSerializer


class MessageListView(CreateAPIView):
    queryset = SendMessagesModel.objects.all()
    serializer_class = MessageSerializer
