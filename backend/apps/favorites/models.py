from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Favorite(models.Model):
    user = models.ForeignKey(
        User, verbose_name='Владелец',
        on_delete=models.CASCADE,
        related_name='favorites'
    )

    total_products = models.PositiveIntegerField('Всего продуктов', default=0)

    def count_totals(self):
        self.total_products = len(self.favorite_products.all())

    def count_totals_and_save(self):
        self.count_totals()
        self.save()

    def __str__(self):
        return self.user.username


class FavoriteProduct(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favorite_products')
    favorite = models.ForeignKey(
        Favorite, on_delete=models.CASCADE, related_name='favorite_products')

    product = models.ForeignKey(
        'catalog.Product',
        on_delete=models.CASCADE,
        related_name='favorite_products'
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.favorite.count_totals_and_save()
        self.product.count_favorites_number_and_save()

    def __str__(self):
        return '{} => {}'.format(self.product.title, self.user.username)
