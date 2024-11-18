FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Открываем порт для работы приложения
EXPOSE 8000

# Команда для запуска приложения
CMD ["gunicorn", "mycego.wsgi:application", "--bind", "0.0.0.0:8000"]