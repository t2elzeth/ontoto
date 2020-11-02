from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey('auth_app.Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(
        'CartProduct',
        verbose_name='Продукты',
        blank=True,
        related_name='related_cart'
    )
    total_products = models.PositiveIntegerField('Всего продуктов', default=0)
    total_price = models.DecimalField(verbose_name='Общая цена', default=0, decimal_places=2, max_digits=9)
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class CartProduct(models.Model):
    user = models.ForeignKey('auth_app.Customer', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField('Количество')
    final_price = models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая цена', default=0)

    def __str__(self):
        return '{} => {}'.format(self.content_type.title, self.user.username)
