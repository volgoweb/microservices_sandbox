class ProductEntity(object):
    def __init__(self, id, name, supplier_id):
        self.id = id
        self.name = name
        self.supplier_id = supplier_id
        self.supplier = None


class Modification(object):
    def __init__(self, id, product_id, name):
        self.id = id
        self.product_id = product_id
        self.name = name
