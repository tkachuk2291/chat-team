from rest_framework import viewsets

from chat.models import Chat, Category
from chat.serializers import ChatSerializer, CategorySerializer, ChatCreateSerializer


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
