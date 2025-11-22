from django.core.management.base import BaseCommand
from telegram_bot.bot_handler import TelegramBotHandler


class Command(BaseCommand):
    help = "Запуск Telegram-бота"

    def handle(self, *args, **options):
        bot = TelegramBotHandler()
        bot.start_polling()
