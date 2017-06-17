from .aggregates import Cart
from .repositories import CartRepo
from infrastructure.exceptions import CartNotExists


def get_cart(user_id: int) -> Cart:
    try:
        cart = CartRepo.get_by_user_id(user_id)
    except CartNotExists:
        cart = CartRepo.create(user_id)
    return cart
