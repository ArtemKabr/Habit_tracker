# users/urls.py — маршруты для регистрации и профиля

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, ProfileView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),

    # Исправленный маршрут (добавлен pk + правильное name)
    path("profile/<int:pk>/", ProfileView.as_view(), name="user_profile"),

    # JWT маршруты
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]