from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Generator
import os

# Получение URL базы данных из переменных окружения
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/chat_db")

# Создание объекта engine для подключения к базе данных
engine = create_engine(DATABASE_URL)

# Создание SessionLocal для создания новых сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание базового класса для моделей
Base = declarative_base()

def get_db() -> Generator:
    """
    Создает и возвращает объект сессии базы данных.
    Используется как зависимость в маршрутах FastAPI для получения сессии.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

