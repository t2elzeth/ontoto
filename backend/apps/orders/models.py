from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders')
    cart = models.ForeignKey(
        'cart.Cart', on_delete=models.CASCADE, related_name='orders')
    receiver = models.ForeignKey(
        'Receiver', on_delete=models.CASCADE, related_name='orders', blank=True, null=True)

    date_created = models.DateTimeField(auto_now=True)

    # TODO: How to implement setting custom receiver or setting user itself as a receiver
    # TODO: How to implement `order_is_delivered` functionality


# TODO: Think on whether create `OrderProduct` model or not

class Receiver(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255)

    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return 'Receiver: {}'.format(self.first_name)
