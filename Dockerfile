# Используем базовый образ с Python
FROM python:3.9

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем все файлы в рабочую директорию контейнера
COPY ../.. .

# Указываем команду для запуска приложения
CMD ["python", "hash_flask.py"]
