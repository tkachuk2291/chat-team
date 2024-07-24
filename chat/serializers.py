from rest_framework import serializers

from chat.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', "email", "nickname")
