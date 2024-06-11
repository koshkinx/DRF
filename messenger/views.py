from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.chats.all()


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        chat_id = self.request.query_params.get('chat_id')
        if chat_id:
            return Message.objects.filter(chat__id=chat_id, chat__participants=self.request.user)
        return Message.objects.filter(chat__participants=self.request.user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
