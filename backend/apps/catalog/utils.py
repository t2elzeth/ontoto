class ProductUtils:
    __ALLOWED_METHODS = ('inc', 'dec')

    @classmethod
    def update_orders_number(cls, instance, operation=""):
        if operation not in cls.__ALLOWED_METHODS:
            raise ValueError('Method must be one of {}'.format(' '.join(cls.__ALLOWED_METHODS)))

        method = {
            'inc': lambda: instance.qty + 1,
            'dec': lambda: instance.qty - 1,
        }.get(operation)

        instance.qty = method()
