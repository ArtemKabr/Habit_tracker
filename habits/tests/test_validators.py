# habits/tests/test_validators.py — тесты валидаторов

import pytest
from rest_framework.exceptions import ValidationError
from habits.validators import (
    validate_reward_and_related_habit,
    validate_duration,
    validate_periodicity,
)


def test_validate_reward_and_related_habit():
    """Ошибка, если указаны reward + related_habit одновременно"""
    data = {
        "reward": "шоколадка",
        "related_habit": object()
    }

    with pytest.raises(ValidationError):
        validate_reward_and_related_habit(data)


def test_validate_duration():
    """Ошибка, если длительность > 120"""
    data = {"duration": 200}

    with pytest.raises(ValidationError):
        validate_duration(data)


def test_validate_periodicity():
    """Ошибка при периодичности вне 1–7"""
    data = {"periodicity": 10}

    with pytest.raises(ValidationError):
        validate_periodicity(data)
