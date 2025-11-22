# telegram_bot/views.py — привязка Telegram и тестовое уведомление
import random
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TelegramConnectSerializer
from .client import TelegramClient
from users.models import User

class TelegramConnectView(generics.GenericAPIView):
    """Принимает chat_id и привязывает его к текущему пользователю."""

    serializer_class = TelegramConnectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # тестовое уведомление
        client = TelegramClient()
        client.send_message(user.telegram_chat_id, "Telegram подключён успешно!")

        return Response({"status": "ok", "message": "Телеграм привязан"})


class GenerateTelegramCodeView(APIView):
    """Создаёт одноразовый код для привязки Telegram."""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        code = str(random.randint(1000, 9999))
        user.telegram_verify_code = code
        user.save()

        return Response({"telegram_code": code})
