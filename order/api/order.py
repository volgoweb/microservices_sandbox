import requests
import json
from domain.services import get_cart
from infrastructure.adapters.products import get_products_short_detail

items = {
    0: {"name": "name1", "supplier_id": 0},
    1: {"name": "name2", "supplier_id": 1},
}


def get_cart(user_id: int) -> dict:
    result = {}
    cart = get_cart(user_id)
    items = cart.get_items()
    products_data = get_products_short_detail([i.product_id for i in items])
    products_data_by_id = {d['id']: d for d in products_data}
    for item in items:
        item_data = {
            'id': item.id,
            'product_id': item.product_id,
            'quantity': item.quantity,
            'product': products_data_by_id.get(item.product_id),
        }
        result.append(item_data)

    return result


def add_item_to_cart(data: dict) -> bool:
    return True


def set_quantity_to_item(item_id: int, quantity: int) -> bool:
    return True


def switch_cart_to_payment_status(item_id: int, quantity: int) -> bool:
    return True


def send_msg(msg=''):
    import pika

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='product', type='fanout')

    channel.basic_publish(exchange='product', routing_key='', body=msg)
    print(" [x] Sent %r" % msg)
    connection.close()
