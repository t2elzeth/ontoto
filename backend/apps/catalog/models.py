import logging
import os

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from utils.decorators import control_save

User = get_user_model()


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subcategories', blank=True, null=True)
    title = models.CharField(verbose_name='Название', max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return '{}, ({})'.format(self.title, self.slug)


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    available = models.BooleanField(verbose_name='Наличие', default=False)

    price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=9)
    old_price = models.DecimalField(verbose_name='Старая цена', decimal_places=2, max_digits=9, default=0)

    orders_number = models.PositiveIntegerField(verbose_name='Кол-во покупок', default=0)
    favorites_number = models.PositiveIntegerField(verbose_name='Кол-во избранных', default=0)

    date_created = models.DateField(default=timezone.now)

    @control_save
    def update_orders_number(self, *args, **kwargs):
        self.orders_number += 1

    @control_save
    def count_favorites_number(self, *args, **kwargs):
        self.favorites_number = len(self.favorite_products.all())

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    """Model to store product's images"""

    # TODO: Use this model
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(blank=True, null=True, upload_to='media/images/')

    def __str__(self):
        return self.product.title

    def image_name(self):
        return os.path.basename(self.image.name)
