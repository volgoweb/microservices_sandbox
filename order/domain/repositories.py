from .aggregates import Order
from .entities import Item

dummy_orders = {
    1: {
        'id': 1,
        'user_id': 1
    },
    2: {
        'id': 2,
        'user_id': 2,
    },
}

dummy_items = {
    1: {
        'id': 1,
        'order_id': 1,
        'product_id': 1,
        'quantity': 1,
        'price': 10,
    },
    2: {
        'id': 2,
        'order_id': 1,
        'product_id': 2,
        'quantity': 3,
        'price': 20,
    },
    3: {
        'id': 3,
        'order_id': 2,
        'product_id': 2,
        'quantity': 9,
        'price': 20,
    },
}


class IOrderRepo(object):
    def get_by_id(self, id_: int) -> Order:
        raise NotImplementedError


class OrderRepo(IOrderRepo):
    def get_by_id(self, id_: int) -> Order:
        d = dummy_orders.get(id_, {})
        order = Order(
            id=d['id'],
            user_id=d['user_id'],
        )
        self._populate_items_to_order(order)
        return order

    def _populate_items(self, order: Order):
        items = self._get_items(order.id)
        order.add_items(items)

    def _get_items(self, order_id: int) -> list:
        items = []
        for d in dummy_items.values():
            if d['order_id'] == order_id:
                item = Item(
                    id=d['id'],
                    product_id=d['product_id'],
                    quantity=d['quantity'],
                    price=d['price'],
                )
                items.append(item)
        return items
