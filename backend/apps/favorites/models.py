from django.contrib.auth import get_user_model
from django.db import models

from utils.decorators import control_save

User = get_user_model()


class Favorite(models.Model):
    user = models.ForeignKey(
        User, verbose_name='Владелец',
        on_delete=models.CASCADE,
        related_name='favorites'
    )
    total_products = models.PositiveIntegerField('Всего продуктов', default=0)

    @control_save
    def count_totals(self, *args, **kwargs):
        self.total_products = len(self.favorite_products.all())

    def __str__(self):
        return self.user.get_username()


class FavoriteProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_products')
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE, related_name='favorite_products')

    product = models.ForeignKey(
        'catalog.Product',
        on_delete=models.CASCADE,
        related_name='favorite_products'
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.favorite.count_totals(save=True)
        self.product.count_favorites_number(save=True)

    def __str__(self):
        return '{} => {}'.format(self.product.title, self.user.get_username())
