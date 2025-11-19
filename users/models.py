# users/models.py — кастомная модель пользователя и менеджер

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """Менеджер пользователей для создания обычных и суперпользователей."""

    def create_user(self, email, password=None, **extra_fields):
        """Создаёт обычного пользователя."""
        if not email:
            raise ValueError("Поле email обязательно")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Создаёт суперпользователя."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("У суперпользователя is_staff должно быть True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("У суперпользователя is_superuser должно быть True")

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Кастомная модель пользователя с авторизацией по email."""

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=True)  # (я добавил)
    last_name = models.CharField(max_length=50, blank=True)  # (я добавил)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    telegram_chat_id = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="ID чата пользователя в Telegram для отправки уведомлений",
    )  # (я добавил)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        """Возвращает строковое представление пользователя."""
        return self.email
