# Dockerfile
FROM python:3.11-slim

WORKDIR /usr/src/app/

RUN pip install --upgrade pip

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        gcc \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN find . -type d -name '__pycache__' -exec rm -rf {} + 2>/dev/null || true
RUN find . -type f -name '*.pyc' -delete

# Переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
