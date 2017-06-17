class OrderNotExists(Exception):
    """ Order entity not found. """
    def __init__(self, order_id, *args, **kwargs):
        self.order_id = order_id
        self.user_id = kwargs.pop('user_id', None)

    def __str__(self, *args, **kwargs):
        """ Return str(self). """
        return 'Order#{oid} of user#{uid} not found'.format(
            oid=self.order_id,
            uid=self.user_id,
        )
