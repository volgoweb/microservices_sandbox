from .aggregates import Order
from .entities import Item
from .repositories import OrderRepo
from infrastructure.exceptions import OrderNotExists
from infrastructure.adapters import cart as cart_adapter
from infrastructure.adapters import sales as sales_adapter
from infrastructure.dto import SaleInfoDTO


class CreateOrderFromCart(object):
    def __init__(self, cart_id: int, user_id: int=None):
        self.cart_id = cart_id
        self.user_id = user_id

    def run(self):
        cart = self.get_cart(self.cart_id)
        order = self.create_order(self.user_id, cart['items'])
        sales_service = ApplySales()
        sales_service.run(order)

    def get_cart(self, cart_id: int) -> dict:
        cart = cart_adapter.get_cart(cart_id)
        return cart

    def create_order(self, user_id, cart_items) -> Order:
        order = Order(user_id)
        OrderRepo.save(order)
        for cart_item in cart_items:
            item = Item(
                order_id=order.id,
                product_id=cart_item['product_id'],
                quantity=cart_item['quantity'],
                price=cart_item['price'],
            )
            order.add_item(item)
        return order


class ApplySales(object):
    def __init__(self):
        self.sales_info = []

    def run(self, order: Order):
        sales_dto = sales_adapter.get_sales_for_order(Order)
        order.set_summary_price(sales_dto.new_summary_price)
        for sale in sales_dto.sales:
            info = SaleInfoDTO(discount=sale.discount, sale_type=sale.type)
            self.sales_info.append(info)
