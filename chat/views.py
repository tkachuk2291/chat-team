from django.contrib.messages.storage.cookie import MessageSerializer
from rest_framework import viewsets

from chat.models import Chat, Category, Message
from chat.serializers import ChatSerializer, CategorySerializer, ChatCreateSerializer, MessageChatSerializer, \
    MessageChatCreateSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    model = Chat
    serializer_class = ChatSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ChatSerializer
        elif self.action == "create":
            return ChatCreateSerializer
        return ChatSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    model = Category
    serializer_class = CategorySerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    model = Message
    serializer_class = MessageChatSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MessageChatSerializer
        elif self.action == "create":
            return MessageChatCreateSerializer
        return MessageChatSerializer

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
