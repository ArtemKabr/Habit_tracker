# telegram_bot/urls.py — маршруты интеграции Telegram

from django.urls import path
from .views import TelegramConnectView, GenerateTelegramCodeView

urlpatterns = [
    path("connect/", TelegramConnectView.as_view(), name="telegram_connect"),
    path("generate-code/", GenerateTelegramCodeView.as_view(), name="generate_telegram_code"),
]
