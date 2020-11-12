import datetime

from rest_framework import serializers

from . import models


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = [
            'category', 'subcategory',
            'title', 'description', 'price',
        ]


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = [
            'category', 'subcategory',
            'title', 'description',
            'price', 'old_price', 'available',
            'orders_number', 'favorites_number', 'changes_number',
            'date_created'
        ]


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = [
            'category', 'subcategory',
            'title', 'description',
            'price', 'old_price', 'available',
            'orders_number', 'favorites_number', 'changes_number',
            'date_created', 'date_last_changed'
        ]

    def update(self, instance, validated_data: dict):
        if not instance.price == validated_data.get('price'):
            validated_data['old_price'] = instance.price

        validated_data['changes_number'] += 1
        validated_data['date_last_changed'] = datetime.date.today()
        return super().update(instance, validated_data)
