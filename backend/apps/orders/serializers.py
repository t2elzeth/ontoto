from rest_framework import serializers

from . import models


class OrderListRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = [
            'id', 'cart', 'is_gift', 'receiver', 'date_created'
        ]


class OrderCreateSerializer(serializers.ModelSerializer):
    full_name = serializers.ModelField(
        model_field=models.Receiver()._meta.get_field('full_name')
    )
    email = serializers.ModelField(
        model_field=models.Receiver()._meta.get_field('email')
    )
    phone = serializers.ModelField(
        model_field=models.Receiver()._meta.get_field('phone')
    )
    address = serializers.ModelField(
        model_field=models.Receiver()._meta.get_field('address')
    )
    postal_code = serializers.ModelField(
        model_field=models.Receiver()._meta.get_field('postal_code')
    )

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
