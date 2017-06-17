from .entities import Modification
from .repositories import ModificationRepo


class AddModification(object):
    def run(self, product_id, name):
        m = Modification(
            id=None,
            product_id=product_id,
            name=name,
        )
        ModificationRepo.save(m)