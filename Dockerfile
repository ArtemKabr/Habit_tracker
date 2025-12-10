# Dockerfile — образ backend для Habit Tracker

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Системные пакеты для сборки зависимостей (если есть wheel'ы на C)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

# Копируем файлы зависимостей
COPY pyproject.toml poetry.lock* /app/

# Устанавливаем зависимости проекта (без создания .venv)
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Копируем весь проект в образ
COPY . /app/

# Порт приложения (для информации)
EXPOSE 8000

# Команду запуска задаём в docker-compose, здесь не указываем
