from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
class Favorite(models.Model):
    user = models.ForeignKey('auth_app.Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(
        'FavoriteProduct',
        verbose_name='Продукты',
        blank=True,
        related_name='related_favorite'
    )
    total_products = models.PositiveIntegerField('Всего продуктов', default=0)

    def __str__(self):
        return self.user.username


class FavoriteProduct(models.Model):
    user = models.ForeignKey('auth_app.Customer', on_delete=models.CASCADE)
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE, related_name='related_favorites')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return '{} => {}'.format(self.content_type.title, self.user.username)
