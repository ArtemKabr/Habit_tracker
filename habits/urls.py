# habits/urls.py — маршруты привычек

from django.urls import path
from .views import (
    HabitListCreateView,
    HabitRetrieveUpdateDeleteView,
    PublicHabitListView,
)

urlpatterns = [
    path("", HabitListCreateView.as_view(), name="habit_list_create"),
    path("<int:pk>/", HabitRetrieveUpdateDeleteView.as_view(), name="habit_detail"),
    path("public/", PublicHabitListView.as_view(), name="habit_public"),
]
