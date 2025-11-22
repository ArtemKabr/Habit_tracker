# telegram_bot/bot_handler.py — обработка команд Telegram бота

import os
import requests
from users.models import User
from telegram_bot.client import TelegramClient


class TelegramBotHandler:
    """Обработчик Telegram-сообщений."""

    def __init__(self):
        self.token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.api_url = f"https://api.telegram.org/bot{self.token}"
        self.client = TelegramClient()
        self.last_update_id = None

    def get_updates(self):
        """Получение обновлений с учётом offset, чтобы избежать спама."""
        params = {}
        if self.last_update_id:
            params["offset"] = self.last_update_id + 1

        response = requests.get(f"{self.api_url}/getUpdates", params=params)
        return response.json()

    def process_updates(self):
        """Обработка входящих обновлений."""
        updates = self.get_updates()

        if "result" not in updates:
            return

        for update in updates["result"]:
            # фиксируем последний update_id
            self.last_update_id = update["update_id"]

            message = update.get("message")
            if not message:
                continue

            chat = message.get("chat")
            text = message.get("text")
            if not chat or not text:
                continue

            chat_id = chat["id"]

            if text == "/start":
                self.handle_start(chat_id)

            if text.startswith("/connect"):
                self.handle_connect(chat_id, text)

    def handle_start(self, chat_id):
        """Приветствие."""
        self.client.send_message(
            chat_id,
            "Привет! Чтобы привязать Telegram, зайдите в профиль Habit Tracker "
            "и нажмите «Получить код». Затем отправьте:\n\n"
            "/connect <код>"
        )

    def handle_connect(self, chat_id, text):
        """Привязка через verify-код."""
        parts = text.split()
        if len(parts) != 2:
            self.client.send_message(chat_id, "Использование: /connect 1234")
            return

        code = parts[1]

        try:
            user = User.objects.get(telegram_verify_code=code)
        except User.DoesNotExist:
            self.client.send_message(chat_id, "Неверный код. Попробуйте снова.")
            return

        user.telegram_chat_id = chat_id
        user.telegram_verify_code = None
        user.save()

        self.client.send_message(chat_id, "Telegram успешно привязан! 🎉")

    def start_polling(self):
        """Запускает бесконечный polling."""
        import time
        print("🚀 Telegram бот запущен (polling)...")

        while True:
            try:
                self.process_updates()
            except Exception as e:
                print(f"Ошибка в polling: {e}")

            time.sleep(1)
