from ..dto import OrderSalesDTO
from domain.aggregates import Order


def get_sales_for_order(order: Order) -> OrderSalesDTO:
    """Requests to sales microservice information about all sales for particular order."""
    pass
