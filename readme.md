# Телеграм-бот
## Стек технологий:
* Aiogram 3
* SQLAlchemy (PostgreSQL)
* Docker
## Запуск локально:
 1. Поднять контейнер с бд:
    ```bash
    docker compose up -d
2. Активировать виртуальную среду, поставить зависимости:
    ```bash
   cd bot
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
3. Запустить бота:
    ```bash
   python main.py