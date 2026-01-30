Chat API — Django + PostgreSQL в Docker

Этот проект представляет собой API на Django, DRF, запускаемое в контейнерах Docker с использованием PostgreSQL в качестве базы данных.

Технологии

- Django — веб-фреймворк
- PostgreSQL — реляционная БД
- Docker — контейнеризация
- docker-compose — оркестрация сервисов


Запуск проекта в Docker

1. Склонируйте репозиторий:

   ```bash
   git clone https://github.com/Romalbj/chat_API_rep.git
   cd chat_API

2. Создайте файл .env в корне проекта:

   ```python
    DB_NAME=chat_api
    DB_USER=chat_admin
    DB_PASSWORD=admin_of_chat
    DB_HOST=db
    DJANGO_SECRET_KEY=django-insecure-jz0rruqvmp%-rf%jq3ti&9j5q-5$(kd$tm5ht6gb8^#_q*70m

3. В файле settings.py закомментить подключение к бд # PostgesDB for local и раскомментить # PostgesDB for Docker   

4. Запустите контейнеры:

 ```bash
  docker-compose up --build
