# Используйте базовый образ Python
FROM python:3.9

# Устанавливаем переменную окружения для указания, что работаем в режиме продакшн
ENV DJANGO_SETTINGS_MODULE=CargoProject.core.settings

# Создаем и устанавливаем рабочий каталог
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код проекта в контейнер
COPY . /app/

# Запускаем команду для сборки статических файлов (если необходимо)
RUN python manage.py collectstatic --noinput

# Определите порт, на котором ваше приложение будет работать
EXPOSE 8000

# Запуск команды для запуска приложения
CMD ["gunicorn", "CargoProject.wsgi:application", "--bind", "0.0.0.0:8000"]
