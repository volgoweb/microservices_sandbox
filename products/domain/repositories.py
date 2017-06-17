from .entities import ProductEntity, ModificationEntity
dummy_products = {
    1: {
        'id': 1,
        'name': 'product 1',
        'supplier_id': 1,
    },
    2: {
        'id': 2,
        'name': 'product 2',
        'supplier_id': 2,
    },
    3: {
        'id': 3,
        'name': 'product 3',
        'supplier_id': 3,
    },
}

dummy_modifications = {
    1: {
        'id': 1,
        'name': 'mod 1',
        'product_id': 1,
    },
    2: {
        'id': 2,
        'name': 'mod 2',
        'product_id': 2,
    },
    3: {
        'id': 3,
        'name': 'mod 3',
        'product_id': 3,
    },
}


class ProductRepo(object):
    def get_by_id(self, id: int):
        p = dummy_products.get(id, {})
        pe = ProductEntity(initial=p)
        return pe

    def all(self):
        entities = []
        for p in dummy_products:
            pe = ProductEntity(initial=p)
            entities.append(pe)
        return entities


class ModificationRepo(object):
    def save(self, m: ModificationEntity):
        max_id = max(dummy_modifications.keys())
        new_id = max_id + 1
        dummy_modifications[new_id] = {
            'id': m.id,
            'product_id': m.product_id,
            'name': m.name,
        }

