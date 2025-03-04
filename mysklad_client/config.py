import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    Класс конфигурации для управления переменными окружения и значениями по умолчанию.

    Атрибуты:
        DB_NAME (str): Имя базы данных.
        DB_USERNAME (str): Имя пользователя базы данных.
        DB_PASSWORD (str): Пароль базы данных.
        DB_HOST (str): Хост базы данных.
        DB_PORT (str): Порт базы данных.
        API_ACCESS_TOKEN (str): Токен доступа к API.
    """
    DB_NAME = os.getenv("DB_NAME", "default_db_name")
    DB_USERNAME = os.getenv("DB_USERNAME", "default_db_user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "default_db_password")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    CREDENTIALS = os.getenv("CREDENTIALS")
