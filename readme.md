
## Запуск

### Установка зависимостей

```bash
poetry install
````

### Активация виртуального окружения

```bash
poetry shell
```

### Запуск бэка

```bash
cd backend
uvicorn app.main:app --reload
```

* Открыть в браузере: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Структура проекта

```
python-bot/
├── backend/
│   ├── api
│   ├── core
│   ├── models
│   ├── schemas
│   ├── services
│   └── main.py      
├── bot
│   ├── data
│   ├── db
│   ├── handlers
│   ├── keyboards
│   ├── states
│   ├── create_bot.py
│   └── main.py    
├── initdb
├── docker-compose.yml
└── README.md
```

---

## Примечания

* Флаг `--reload` включает автоматическую перезагрузку при изменениях (для разработки).
* Все зависимости указаны в `pyproject.toml`.
