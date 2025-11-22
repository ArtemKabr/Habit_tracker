# users/views.py — вьюхи регистрации и профиля

from rest_framework import generics, permissions
from .serializers import RegisterSerializer, UserSerializer
from .models import User


class RegisterView(generics.CreateAPIView):
    """Регистрация пользователя."""
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class ProfileView(generics.RetrieveUpdateAPIView):
    """Просмотр и редактирование профиля текущего пользователя."""
    serializer_class = UserSerializer

    def get_object(self):
        """Возвращает текущего пользователя."""
        return self.request.user
