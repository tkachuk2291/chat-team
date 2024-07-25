from django.contrib.auth import get_user_model
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
        fields = ('id', "name", "date_created", "category")

    def create(self, validated_data):
        users = validated_data.pop('users', [])
        chat = Chat.objects.create(**validated_data)
        chat.users.set(users)  # Use set() for ManyToManyField
        return chat


class UserChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()

        fields = ("id", 'email',)


class UserChatSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Chat

        fields = ('id', "name", "category",)


class MessageChatSerializer(serializers.ModelSerializer):
    user = UserChatMessageSerializer()
    chat = UserChatSerializer()

    class Meta:
        model = Message
        fields = ('id', "user", "date_created", "text", "chat")


class MessageChatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', "chat", "text", "date_created")

    def create(self, validated_data):
        return Message.objects.create(**validated_data)
