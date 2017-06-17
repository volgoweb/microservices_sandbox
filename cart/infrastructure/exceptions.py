class CartNotExists(Exception):
    """ Cart entity not found. """
    def __init__(self, user_id, *args, **kwargs):
        self.user_id = user_id

    def __str__(self, *args, **kwargs):
        """ Return str(self). """
        return 'Cart of user#%d not found' % self.user_id
