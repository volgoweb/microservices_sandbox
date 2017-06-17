import requests
import json

items = {
    0: {"name": "name1", "supplier_id": 0},
    1: {"name": "name2", "supplier_id": 1},
}


class Catalog(object):
    def get(self):
        return items

catalog_instance = Catalog()


def product_detail(id: int) -> dict:
    send_msg('read product %d' % id)
    item = items[id]
    resp = requests.get('http://127.0.0.1:5002/v1.0/suppliers/%d' % item['supplier_id'])
    sup = json.loads(resp.text)
    item['supplier'] = sup
    return item


def create_product():
    send_msg('created product!!!')
    return True


def send_msg(msg=''):
    import pika

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='product', type='fanout')

    channel.basic_publish(exchange='product', routing_key='', body=msg)
    print(" [x] Sent %r" % msg)
    connection.close()
