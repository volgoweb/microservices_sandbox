from .aggregates import Cart
from .entities import Item

dummy_carts = {
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
        'cart_id': 1,
        'product_id': 1,
        'quantity': 1,
    },
    2: {
        'id': 2,
        'cart_id': 1,
        'product_id': 2,
        'quantity': 3,
    },
    3: {
        'id': 3,
        'cart_id': 2,
        'product_id': 2,
        'quantity': 9,
    },
}


class ICartRepo(object):
    def get_by_user_id(self, user_id: int) -> Cart:
        raise NotImplementedError


class CartRepo(ICartRepo):
    def get_by_user_id(self, user_id: int) -> Cart:
        d = dummy_carts.get(user_id, {})
        cart = Cart(
            id=d['id'],
            user_id=d['user_id'],
        )
        self._populate_items_to_cart(cart)
        return cart

    def _populate_items(self, cart: Cart):
        items = self._get_items(cart.id)
        cart.add_items(items)

    def _get_items(self, cart_id: int) -> list:
        items = []
        for d in dummy_items.values():
            if d['cart_id'] == cart_id:
                item = Item(
                    id=d['id'],
                    product_id=d['product_id'],
                    quantity=d['quantity'],
                )
                items.append(item)
        return items
