# habits/tasks.py — задачи Celery

from celery import shared_task
from django.utils import timezone
from habits.models import Habit
from telegram_bot.client import TelegramClient


@shared_task
def send_habit_notifications():
    """Рассылает уведомления по привычкам."""
    now = timezone.localtime().strftime("%H:%M")
    client = TelegramClient()

    habits = Habit.objects.filter(time=now)

    for habit in habits:
        user = habit.user
        if user.telegram_chat_id:
            message = f"Напоминание: {habit.action} в {habit.place}"
            client.send_message(user.telegram_chat_id, message)
