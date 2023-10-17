# Используем официальный образ Python 3.10
FROM python:3.10

# Устанавливаем переменные окружения
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Устанавливаем рабочий каталог внутри контейнера
WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Копируем остальное приложение
COPY . /app/

# Устанавливаем django-cors-headers
RUN pip install django-cors-headers
RUN python manage.py migrate

# Команда для запуска Django-сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
