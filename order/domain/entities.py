class Item(object):
    def __init__(self, id_: int, product_id: int, quantity: int, price: float):
        self.id = id_
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
