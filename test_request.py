from mysklad_client.http_client import HTTP_CLIENT

def get_purchase_orders():
    """
    Функция для получения списка заказов на поставку.
    Возвращает: list заказов.
    """
    response = HTTP_CLIENT.get(endpoint="entity/purchaseorder")
    orders = response.get("rows", [])
    return orders

orders = get_purchase_orders()
print(orders)