import os

from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(verbose_name='', max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return '{}, ({})'.format(self.title, self.slug)

class Subcategory(Category):
    parent = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', blank=True, null=True)

    def __str__(self):
        return '{}, ({})'.format(self.title, self.slug)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_products')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, related_name='subcategory_products')

    title = models.CharField(verbose_name='', max_length=255)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    available = models.BooleanField(verbose_name='Наличие', default=False)

    price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=9)
    old_price = models.DecimalField(verbose_name='Старая цена', decimal_places=2, max_digits=9, default=0)

    orders_number = models.PositiveIntegerField(verbose_name='Кол-во покупок', default=0)
    favorites = models.PositiveIntegerField(verbose_name='Кол-во избранных', default=0)
    changes_number = models.PositiveIntegerField(verbose_name='Кол-во изменений', default=0)

    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(blank=True, null=True, upload_to='media/')

    def __str__(self):
        return self.product.title

    def image_name(self):
        return os.path.basename(self.image.name)
