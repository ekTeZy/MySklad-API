"""
Модуль для получения и сохранения заказов.

Функции:
    fetch_and_save_supplier_orders(): Получает список заказов из внешнего API и сохраняет их в базу данных.
"""

from mysklad_client.db_client import DatabaseClient
from mysklad_client.http_client import HTTP_CLIENT
from mysklad_client.models import SupplierOrder
from structlog import get_logger
from datetime import datetime

logger = get_logger()

def fetch_and_save_supplier_orders():
    """
    Получает список заказов поставщиков из внешнего API и сохраняет их в базу данных.

    Шаги:
    1. Отправляет запрос к API для получения списка заказов.
    2. Проверяет, есть ли новые заказы для обработки.
    3. Если есть новые заказы, создает сессию базы данных.
    4. Для каждого заказа проверяет, существует ли он уже в базе данных.
    5. Если заказ не существует, создает новый объект SupplierOrder и добавляет его в базу данных.
    6. Фиксирует изменения в базе данных.
    7. Закрывает сессию базы данных.
    """
    logger.info("Запрос списка заказов...")

    try:
        response = HTTP_CLIENT.get(endpoint="entity/purchaseorder")
        orders = response.get("rows", [])

        if not orders:
            logger.info("Нет новых заказов для обработки.")
            return

        session = DatabaseClient.get_db_session()

        for order in orders:
            existing_order = session.query(SupplierOrder).filter_by(order_id=order["id"]).first()

            if existing_order:
                logger.info(f"Заказ {order['name']} уже существует в БД")
                continue

            new_order = SupplierOrder(
                order_id=order["id"],
                name=order.get("name", "Без названия"),
                date=datetime.strptime(order.get("moment"), "%Y-%m-%d %H:%M:%S.%f") if order.get("moment") else None,
                counterparty=order.get("agent", {}).get("meta", {}).get("href", ""),
                organization=order.get("organization", {}).get("meta", {}).get("href", ""),
                sum=order.get("sum", 0),
                description=order.get("description", ""),
                state=order.get("state", {}).get("meta", {}).get("href", ""),
                delivery_date=datetime.strptime(order.get("deliveryPlannedMoment"), "%Y-%m-%d %H:%M:%S.%f") if order.get("deliveryPlannedMoment") else None,
                payed_sum=order.get("payedSum", 0),
                shipped_sum=order.get("shippedSum", 0),
                invoiced_sum=order.get("invoicedSum", 0)
            )

            session.add(new_order)
            logger.info(f"Заказ добавлен: {new_order.name}")

        session.commit()
        logger.info("Все заказы сохранены")

    except Exception as e:
        logger.error("Ошибка при обработке", error=str(e))

    finally:
        session.close()

if __name__ == "__main__":
    fetch_and_save_supplier_orders()