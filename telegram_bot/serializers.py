# telegram_bot/serializers.py — сериализатор привязки телеграм-аккаунта

from rest_framework import serializers


class TelegramConnectSerializer(serializers.Serializer):
    """Сериализатор для сохранения chat_id Telegram у пользователя."""
    chat_id = serializers.CharField()

    def save(self, **kwargs):
        user = self.context["request"].user
        user.telegram_chat_id = self.validated_data["chat_id"]
        user.save()
        return user
