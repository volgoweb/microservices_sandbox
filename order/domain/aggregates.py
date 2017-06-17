

class Order(object):
    def __init__(self, id_, user_id):
        self.id = id_
        self.user_id = user_id
        self._items = []

    def add_item(self, item):
        self._items.append(item)
        self.calculate_summary_price

    def get_items(self):
        return self._items

        # def clear(self):
        #     for item in self._items:
        #         ItemRepository.delete(item)

    def set_summary_price(self, value):
        self._summary_price = value

    def get_summary_price(self):
        return self._summary_price

    def calculate_summary_price(self):
        summary = 0
        for item in self._items:
            item_summary = item.price * item.quantity
            summary += item_summary
        self.set_summary_price(summary)


