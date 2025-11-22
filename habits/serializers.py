# habits/serializers.py — сериализатор привычки

from rest_framework import serializers
from .models import Habit
from .validators import (
    validate_reward_and_related_habit,
    validate_duration,
    validate_related_habit_is_pleasant,
    validate_pleasant_habit_rules,
    validate_periodicity,
)


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор привычки с валидацией."""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, data):
        """Запуск всех кастомных валидаторов."""
        validate_reward_and_related_habit(data)
        validate_duration(data)
        validate_related_habit_is_pleasant(data)
        validate_pleasant_habit_rules(data)
        validate_periodicity(data)
        return data
