class ProductUtils:
    __ALLOWED_METHODS = ('inc', 'dec')

    @staticmethod
    def update_orders_number(self, operation=""):
        if operation not in self.__ALLOWED_METHODS:
            raise ValueError('Method must be one of {}'.format(' '.join(self.__ALLOWED_METHODS)))

        method = {
            'inc': lambda: self.qty + 1,
            'dec': lambda: self.qty - 1,
        }.get(operation)

        self.qty = method()
