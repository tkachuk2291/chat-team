from rest_framework import serializers

from chat.models import Chat, Category, Message
from user_account.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', "category")


class ChatSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    users = UserSerializer(many=True)

    class Meta:
        model = Chat
        fields = ('id', "name", "date_created", "category", "users")


class ChatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', "name", "date_created", "category", "users")

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        users_data = validated_data.pop('users')
        chat = Chat.objects.create(category=category_data, **validated_data)
        chat.users.set(users_data)
        return chat


class MessageChatSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    chat = ChatSerializer()

    class Meta:
        model = Message
        fields = ('id', "user", "chat", "text", "date_created")


class MessageChatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', "user", "chat", "text", "date_created")

    def create(self, validated_data):
        return Message.objects.create(**validated_data)
