# habits/validators.py — валидаторы привычек

from rest_framework import serializers


def validate_reward_and_related_habit(data):
    """Нельзя одновременно указывать reward и related_habit."""
    if data.get("reward") and data.get("related_habit"):
        raise serializers.ValidationError(
            "Нельзя одновременно указывать вознаграждение и связанную приятную привычку."
        )


def validate_duration(data):
    """Длительность ≤ 120 секунд."""
    if data.get("duration") and data["duration"] > 120:
        raise serializers.ValidationError(
            "Время выполнения не может превышать 120 секунд."
        )


def validate_related_habit_is_pleasant(data):
    """Связанной привычкой может быть только приятная."""
    habit = data.get("related_habit")
    if habit and not habit.is_pleasant:
        raise serializers.ValidationError(
            "Связанной привычкой может быть только приятная привычка."
        )


def validate_pleasant_habit_rules(data):
    """У приятной привычки нет reward и нет related_habit."""
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
    """Периодичность 1–7 дней."""
    period = data.get("periodicity")
    if period and not (1 <= period <= 7):
        raise serializers.ValidationError(
            "Периодичность должна быть от 1 до 7 дней."
        )