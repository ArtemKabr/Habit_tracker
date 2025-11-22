# users/tests/test_users_api.py — тесты API пользователей

import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from users.models import User


@pytest.mark.django_db
def test_user_registration():
    """Тест регистрации пользователя"""
    client = APIClient()

    data = {
        "email": "testuser@mail.ru",
        "password": "StrongPass123!"
    }

    response = client.post(reverse("register"), data)

    assert response.status_code == 201
    assert User.objects.filter(email="testuser@mail.ru").exists()


@pytest.mark.django_db
def test_user_login():
    """Тест получения JWT токена"""
    User.objects.create_user(email="login@mail.ru", password="pass1234")
    client = APIClient()

    data = {
        "email": "login@mail.ru",
        "password": "pass1234"
    }

    response = client.post(reverse("token_obtain_pair"), data)

    assert response.status_code == 200
    assert "access" in response.data


@pytest.mark.django_db
def test_user_profile_get():
    """Тест получения профиля"""
    user = User.objects.create_user(email="profile@mail.ru", password="1234")
    client = APIClient()
    client.force_authenticate(user=user)

    response = client.get(reverse("user_profile", args=[user.id]))

    assert response.status_code == 200
    assert response.data["email"] == user.email
