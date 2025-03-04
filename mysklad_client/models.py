from sqlalchemy import Column, Integer, Text, Double, TIMESTAMP, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class SupplierOrder(Base):
    """
    Класс, представляющий заказ поставщика.

    Атрибуты:
    - id (Integer): Уникальный идентификатор заказа.
    - order_id (String): Уникальный идентификатор заказа.
    - name (Text): Название заказа.
    - date (TIMESTAMP): Дата создания заказа.
    - counterparty (Text): Контрагент.
    - organization (Text): Организация.
    - sum (Double): Сумма заказа.
    - description (Text): Описание заказа.
    - state (Text): Состояние заказа.
    - delivery_date (TIMESTAMP): Дата доставки.
    - payed_sum (Double): Оплаченная сумма.
    - shipped_sum (Double): Отгруженная сумма.
    - invoiced_sum (Double): Сумма в счете.
    """
    
    
    __tablename__ = "supplier_orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(String, unique=True, nullable=False) 
    name = Column(Text, nullable=False)
    date = Column(TIMESTAMP, nullable=False, server_default=func.now())
    counterparty = Column(Text)
    organization = Column(Text)
    sum = Column(Double, default=0)
    description = Column(Text)
    state = Column(Text)
    delivery_date = Column(TIMESTAMP)
    payed_sum = Column(Double, default=0)
    shipped_sum = Column(Double, default=0)
    invoiced_sum = Column(Double, default=0)
