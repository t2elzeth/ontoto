from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(verbose_name='', max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return '{}, ({})'.format(self.title, self.slug)


class Product(models.Model):
    class Meta:
        abstract = True

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='', max_length=255)
    image = models.ImageField(blank=True, null=True, upload_to='media/')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    price = models.DecimalField(verbose_name='', decimal_places=2, max_digits=9)

    def __str__(self):
        return self.title





class Clothing(Product):
    size = models.PositiveIntegerField(verbose_name='Размер')
    color = models.CharField('Цвет', max_length=255)

    def __str__(self):
        return self.title
