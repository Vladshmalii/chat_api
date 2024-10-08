# FastAPI Chat Application

## Описание проекта

Это простое приложение чата, разработанное с использованием FastAPI. Оно позволяет пользователям регистрироваться, авторизовываться, отправлять и получать сообщения в режиме реального времени. Приложение также использует Docker для упрощения развертывания и управления зависимостями.

## Особенности

- Регистрация и авторизация пользователей.
- Отправка и получение сообщений.
- Использование WebSocket для чата в реальном времени.
- Docker для удобного развертывания.

## Структура проекта

- `app/`: Основной каталог проекта.
  - `main.py`: Главный файл приложения, в котором создается экземпляр FastAPI и настраиваются маршруты.
  - `auth.py`: Модуль для обработки аутентификации и регистрации пользователей.
  - `chat.py`: Модуль для обработки чата и WebSocket-соединений.
  - `database.py`: Модуль для настройки подключения к базе данных.
  - `models.py`: Определение моделей базы данных.
  - `schemas.py`: Определение схем данных для валидации запросов и ответов.
  - `services.py`: Логика взаимодействия с базой данных и другие вспомогательные функции.

## Установка и настройка

1.Создайте и активируйте виртуальное окружение


python -m venv venv
source venv/bin/activate  # На Windows используйте `venv\Scripts\activate`
Установите зависимости

pip install -r requirements.txt
Настройте переменные окружения

Создайте файл .env в корневом каталоге проекта и добавьте следующие переменные:

DATABASE_URL=postgresql://general:general@db:5432/general
Запустите приложение с помощью Docker

Убедитесь, что Docker установлен и запущен. Затем выполните следующие команды:

bash
Копировать код
docker-compose up --build
Это создаст и запустит контейнеры для вашего приложения и базы данных.

Запустите приложение без Docker (опционально)

Если вы предпочитаете запускать приложение без Docker, выполните следующую команду:

uvicorn app.main:app --reload
Убедитесь, что база данных доступна по указанному URL в переменной окружения DATABASE_URL.

Использование

Откройте браузер и перейдите по адресу http://localhost:8000, чтобы увидеть интерфейс приложения.
Используйте предоставленные маршруты для регистрации, авторизации и общения в чате.

Тестирование

Для запуска тестов используйте следующую команду:


pytest