import requests
from .config import Config
from structlog import get_logger

logger = get_logger()

class SupplierOrdersClient:
    """
    Класс для взаимодействия с API.

    Атрибуты:
    BASE_URL (str): Базовый URL для API.
    HEADERS (dict): Заголовки для HTTP-запросов, включая токен доступа и тип контента.

    Методы:
    get(endpoint, params=None): Выполняет GET-запрос к указанному эндпоинту с заданными параметрами.
    _handle_response(response): Обрабатывает ответ от API, логирует ошибки и вызывает исключение при необходимости.
    """
    
    BASE_URL = "https://api.moysklad.ru/api/remap/1.2"
    HEADERS = {
        "Authorization": f"Basic {Config.CREDENTIALS}",
        "Accept-Encoding": "gzip",
        "Content-Type": "application/json"
    }

    @classmethod
    def get(cls, endpoint, params=None):
        url = f"{cls.BASE_URL}/{endpoint}"
        response = requests.get(url, headers=cls.HEADERS, params=params)
        cls._handle_response(response)
        return response.json()

    @classmethod
    def _handle_response(cls, response):
        if response.status_code not in (200, 204):
            logger.error("API request failed",
                        status_code=response.status_code,
                        response_text=response.text)
            response.raise_for_status()

HTTP_CLIENT = SupplierOrdersClient()