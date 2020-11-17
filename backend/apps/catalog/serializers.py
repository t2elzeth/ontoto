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
            'id', 'category', 'subcategory',
            'title', 'description',
            'price', 'old_price', 'available',
            'orders_number', 'favorites_number', 'changes_number',
            'date_created'
        ]
        depth = 2


class ProductRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = [
            'id', 'category', 'subcategory',
            'title', 'description',
            'price', 'old_price', 'available',
            'orders_number', 'favorites_number', 'changes_number',
            'date_created', 'date_last_changed'
        ]
