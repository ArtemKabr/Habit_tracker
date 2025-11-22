# habits/models.py — модель привычки

from django.db import models
from django.conf import settings


class Habit(models.Model):
    """Модель привычки."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="habits",
        verbose_name="Пользователь",
    )

    place = models.CharField(max_length=255, verbose_name="Место")
    time = models.TimeField(verbose_name="Время")
    action = models.CharField(max_length=255, verbose_name="Действие")

    is_pleasant = models.BooleanField(
        default=False,
        verbose_name="Признак приятной привычки",
        help_text="True — если это приятная привычка (вознаграждение)",
    )

    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Связанная привычка",
        help_text="Приятная привычка, выполняемая после полезной",
    )

    periodicity = models.PositiveSmallIntegerField(
        default=1,
        verbose_name="Периодичность выполнения (дни)",
        help_text="От 1 до 7 дней",
    )

    reward = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Вознаграждение",
    )

    duration = models.PositiveIntegerField(
        verbose_name="Время выполнения (сек.)",
        help_text="Не более 120 секунд",
    )

    is_public = models.BooleanField(
        default=False,
        verbose_name="Публичная привычка",
    )

    def __str__(self):
        return f"{self.action} — {self.user.email}"
