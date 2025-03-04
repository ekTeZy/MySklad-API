# MySklad-API

Проект для получения и обработки заказов поставщиков из API МойСклад и сохранения их в базу данных PostgreSQL.

## Установка

1. **Клонировать репозиторий**:
   ```bash
   git clone https://github.com/ekTeZy/MySklad-API.git
   cd MySklad-API
   ```

2. **Создать виртуальное окружение**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  
   ```

3. **Установить зависимости**:
   ```bash
   pip install -r requirements.txt
   ```

## Настройка

Перед запуском создайте файл `.env` в корне проекта и добавьте туда параметры:

```
DB_NAME=mysklad
DB_USERNAME=<db_user>
DB_PASSWORD=<db_password>
DB_HOST=localhost
DB_PORT=5432
CREDENTIALS=<login:password>
```

## Использование

### Получение и сохранение заказов

Запуск основного модуля:
```bash
python main.py
```

### Структура проекта
- `config.py` – Загрузка переменных окружения.
- `db_client.py` – Подключение к базе данных.
- `http_client.py` – Запросы к API МойСклад.
- `models.py` – Описание таблицы заказов.
- `main.py` – Основная логика: получение и сохранение заказов.

## Дополнительно
Базу данных можно создать с помощью `psql`, таким образом можно с ней работать.
```bash
psql -U <db_user> -d mysklad
```
