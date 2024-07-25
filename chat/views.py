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

    def perform_create(self, serializer):
        serializer.save(users=[self.request.user])

    def get_queryset(self):
        queryset = Chat.objects.all()
        chat_name = self.request.query_params.get("chat_name")
        chat_id = self.request.query_params.get("chat_id")
        if chat_name:
            queryset = queryset.filter(
                name__icontains=chat_name
            )
        if chat_name:
            queryset = queryset.filter(
               id=chat_id
            )
        return queryset.distinct()


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
