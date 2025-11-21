# habits/tests/test_habits_api.py — тесты API привычек

import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from habits.models import Habit
from users.models import User


@pytest.mark.django_db
def test_create_habit():
    """Создание привычки"""
    user = User.objects.create_user(email="u@mail.ru", password="1234")
    client = APIClient()
    client.force_authenticate(user=user)

    data = {
        "place": "дом",
        "time": "12:00:00",
        "action": "выпить воду",
        "periodicity": 1,
        "duration": 30,
        "is_public": False,
        "is_pleasant": False,
    }

    response = client.post(reverse("habit_list_create"), data)

    assert response.status_code == 201
    assert Habit.objects.filter(user=user).count() == 1


@pytest.mark.django_db
def test_list_user_habits():
    """Получение списка привычек пользователя"""
    user = User.objects.create_user(email="u2@mail.ru", password="1234")
    Habit.objects.create(
        user=user,
        place="дом",
        time="10:00:00",
        action="зарядка",
        periodicity=1,
        duration=30,
    )

    client = APIClient()
    client.force_authenticate(user=user)

    response = client.get(reverse("habit_list_create"))

    assert response.status_code == 200
    assert len(response.data["results"]) == 1


@pytest.mark.django_db
def test_public_habits():
    """Список публичных привычек"""
    user = User.objects.create_user(email="u3@mail.ru", password="1234")
    Habit.objects.create(
        user=user,
        place="улица",
        time="09:00:00",
        action="прогулка",
        periodicity=1,
        duration=20,
        is_public=True,
    )

    client = APIClient()

    response = client.get(reverse("habit_public"))

    assert response.status_code == 200
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["action"] == "прогулка"
