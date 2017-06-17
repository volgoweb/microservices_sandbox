items = {
    0: {"name": "supplier1"},
    1: {"name": "supplier2"},
}


def all_suppliers():
    return items


def supplier_detail(id: int) -> dict:
    return items[id]
