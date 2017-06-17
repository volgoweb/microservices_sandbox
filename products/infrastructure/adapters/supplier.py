import requests
import json


def get_supplier_data(supplier_id):
    resp = requests.get('http://127.0.0.1:5002/v1.0/suppliers/%d' % supplier_id)
    sup = json.loads(resp.text)
    return sup


def get_supplier_ids_with_shipping_method(shipping_method):
    resp = requests.get('http://127.0.0.1:5002/v1.0/suppliers/....')
    sups = json.loads(resp.text)
    return sups
