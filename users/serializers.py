# users/serializers.py — сериализаторы регистрации и вывода пользователя

from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    """Сериализатор регистрации нового пользователя."""

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name"]

    def create(self, validated_data):
        """Создаёт пользователя через UserManager."""
        password = validated_data.pop("password")
        user = User.objects.create_user(**validated_data, password=password)
        return user


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор просмотра профиля пользователя."""

    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "telegram_chat_id"]
