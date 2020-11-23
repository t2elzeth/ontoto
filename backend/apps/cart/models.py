from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Cart(models.Model):
    """Cart model"""
    user = models.ForeignKey(
        User,
        verbose_name='Владелец',
        on_delete=models.CASCADE,
        related_name='carts'
    )
    total_products = models.PositiveIntegerField('Всего продуктов', default=0)
    total_price = models.DecimalField(verbose_name='Общая цена', default=0, decimal_places=2, max_digits=9)
    in_order = models.BooleanField(default=False)

    def count_totals(self, save=False):
        """
        Counts `total products` and `total price`
        """
        self.total_products = sum(cp.qty for cp in self.cart_products.all())
        self.total_price = sum(cp.final_price for cp in self.cart_products.all())

        if save:
            self.save()

    def __str__(self):
        return "{}'s cart. In order: {}".format(
            self.user.get_username(),
            self.in_order
        )


class CartProduct(models.Model):
    """Cart Product model to save products in Cart"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_products')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_products')

    product = models.ForeignKey(
        'catalog.Product',
        on_delete=models.CASCADE,
        related_name='cart_products'
    )
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey('content_type', 'object_id')

    qty = models.PositiveIntegerField('Количество', default=0)
    final_price = models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая цена', default=0)

    date_added = models.DateTimeField(default=timezone.now)

    def count_final_price(self, save=False):
        """Counts final price, but doesn't save the changes"""
        self.final_price = self.product.price * self.qty

        if save:
            self.save()

    def save(self, *args, **kwargs):
        """Custom save method"""

        # Count final price of CartProduct
        self.count_final_price()
        super().save(*args, **kwargs)

        # Count `total products` and `total_price` in `Cart`
        self.cart.count_totals(save=True)

    def __str__(self):
        return "{} in {}".format(self.product.title, self.cart)
