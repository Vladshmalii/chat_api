# FastAPI Chat Application

Простое чат-приложение на FastAPI с WebSocket, JWT-авторизацией и PostgreSQL.

## Возможности

- Регистрация и авторизация пользователей (JWT)
- Отправка и получение сообщений
- Реальное время через WebSocket
- Docker-контейнеризация

## Стек технологий

- **FastAPI** — веб-фреймворк
- **PostgreSQL** — база данных
- **Docker & Docker Compose** — контейнеризация
- **WebSocket** — реальное время
- **SQLAlchemy** — ORM

## Структура проекта

```
app/
├── main.py          # Точка входа, маршруты
├── auth.py          # Регистрация, авторизация
├── chat.py          # WebSocket, обработка сообщений
├── database.py      # Настройка БД
├── models.py        # Модели SQLAlchemy
├── schemas.py       # Pydantic-схемы
└── services.py      # Бизнес-логика
```

## Быстрый старт

### С Docker (рекомендуется)

1. Клонируйте репозиторий
2. Создайте `.env`:

```env
DATABASE_URL=postgresql://general:general@db:5432/general
SECRET_KEY=your-secret-key
```

3. Запустите:

```bash
docker-compose up --build
```

4. Откройте http://localhost:8000

### Без Docker

1. Создайте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. Установите зависимости:

```bash
pip install -r requirements.txt
```

3. Создайте `.env` с `DATABASE_URL` для локальной БД

4. Запустите:

```bash
uvicorn app.main:app --reload
```

## API Endpoints

| Метод | Endpoint | Описание |
|-------|----------|----------|
| POST | `/register` | Регистрация |
| POST | `/login` | Авторизация (получение JWT) |
| WS | `/ws/chat` | WebSocket для чата |
| GET | `/messages` | История сообщений |

## Тестирование

```bash
pytest
```

## Переменные окружения

| Переменная | Описание | Пример |
|------------|----------|--------|
| `DATABASE_URL` | URL БД | `postgresql://user:pass@host:5432/db` |
| `SECRET_KEY` | Ключ для JWT | `your-secret-key` |

## Разработка

Для разработки используйте горячую перезагрузку:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Docker Compose

Запуск всех сервисов:

```bash
docker-compose up -d
```

Просмотр логов:

```bash
docker-compose logs -f
```

Остановка:

```bash
docker-compose down
```

## Лицензия

MIT
