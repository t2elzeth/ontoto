from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = [
            'id', 'category',
            'title', 'description',
            'price', 'old_price', 'available',
            'orders_number', 'favorites_number',
            'date_created'
        ]
        depth = 2
        read_only_fields = ['id', 'old_price', 'orders_number', 'favorites_number', 'date_created']


class CatalogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = [
            'id', 'parent', 'title', 'slug'
        ]
        depth = 2
