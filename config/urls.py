# config/urls.py — корневые маршруты

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),
    path("api/habits/", include("habits.urls")),
    path("api/telegram/", include("telegram_bot.urls")),
]
