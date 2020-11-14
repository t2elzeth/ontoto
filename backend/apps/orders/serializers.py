import logging

from rest_framework import serializers

from cart.models import Cart
from . import models


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = [
            'id', 'cart', 'is_gift', 'date_created'
        ]


class OrderCreateSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    email = serializers.EmailField(allow_blank=True, allow_null=True)
    phone = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    address = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    postal_code = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)

    class Meta:
        model = models.Order
        fields = [
            'cart',
            'is_gift',
            'date_created',

            # Receiver fields
            'full_name',
            'email',
            'phone',
            'address',
            'postal_code',
        ]


class OrderRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = [
            'id', 'cart', 'is_gift', 'is_closed', 'date_created'
        ]
