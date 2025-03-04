from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import Config



class DatabaseClient:
    """
    Класс для работы с базой данных.

    Атрибуты:
        DATABASE_URL (str): URL для подключения к базе данных.
        engine: Объект движка SQLAlchemy.
        SessionLocal: Фабрика сессий SQLAlchemy.

    Методы: get_db_session() возвращает новую сессию базы данных.
    """
    
    DATABASE_URL = f"postgresql+psycopg2://{Config.DB_USERNAME}:{Config.DB_PASSWORD}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"
    engine = create_engine(DATABASE_URL, echo=False)
    SessionLocal = sessionmaker(bind=engine)

    @classmethod
    def get_db_session(cls):
        return cls.SessionLocal() 