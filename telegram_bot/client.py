# telegram_bot/client.py — клиент Telegram API

import requests
import os


class TelegramClient:
    """Клиент для отправки сообщений через Telegram Bot API."""

    def __init__(self):
        self.token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.base_url = f"https://api.telegram.org/bot{self.token}"

    def send_message(self, chat_id: str, text: str) -> bool:
        """Отправляет сообщение пользователю."""
        url = f"{self.base_url}/sendMessage"
        data = {"chat_id": chat_id, "text": text}

        response = requests.post(url, json=data)

        return response.status_code == 200
