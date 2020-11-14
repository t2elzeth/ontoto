from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders')
    cart = models.ForeignKey(
        'cart.Cart', on_delete=models.CASCADE, related_name='orders')

    is_gift = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}'s order. Gift: {}".format(self.user.username, self.is_gift)

    # TODO: How to implement `order_is_delivered` functionality


# TODO: Think on whether create `OrderProduct` model or not

class Receiver(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='receivers')
    full_name = models.CharField(max_length=255)

    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255)

    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return 'Receiver: {}'.format(self.full_name)
