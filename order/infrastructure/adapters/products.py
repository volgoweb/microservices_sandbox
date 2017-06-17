import requests
import json


def get_products_short_detail(product_ids):
    resp = requests.get('http://127.0.0.1:5002/v1.0/products-by-ids/short-detail/', params={
        'ids': product_ids,
    })
    sup = json.loads(resp.text)
    return sup
