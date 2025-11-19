# habits/validators.py — валидаторы привычек

from rest_framework import serializers
from .models import Habit


def validate_reward_and_related_habit(data):
    """
    Проверяет, что не выбраны одновременно reward и related_habit.
    """
    if data.get("reward") and data.get("related_habit"):
        raise serializers.ValidationError(
            "Нельзя одновременно указывать вознаграждение и связанную приятную привычку."
        )


def validate_duration(data):
    """Проверяет, что длительность ≤ 120 секунд."""
    if data.get("duration") and data["duration"] > 120:
        raise serializers.ValidationError(
            "Время выполнения не может превышать 120 секунд."
        )


def validate_related_habit_is_pleasant(data):
    """
    Проверяет, что в related_habit указана только приятная привычка.
    """
    habit = data.get("related_habit")
    if habit and not habit.is_pleasant:
        raise serializers.ValidationError(
            "Связанной привычкой может быть только приятная привычка."
        )


def validate_pleasant_habit_rules(data):
    """
    У приятной привычки (is_pleasant=True) не может быть reward или related_habit.
    """
    if data.get("is_pleasant"):
        if data.get("reward"):
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения."
            )
        if data.get("related_habit"):
            raise serializers.ValidationError(
                "У приятной привычки не может быть связанной привычки."
            )


def validate_periodicity(data):
    """Периодичность должна быть от 1 до 7 дней."""
    period = data.get("periodicity")
    if period and not (1 <= period <= 7):
        raise serializers.ValidationError(
            "Периодичность должна быть от 1 до 7 дней."
        )
