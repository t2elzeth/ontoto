from rest_framework import serializers

from . import models


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = [
            'category', 'title', 'description', 'price',
        ]


class ProductListRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
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

        extra_kwargs = {
            'id': {
                'read_only': True,
            },
            'old_price': {
                'read_only': True,
            },
            'orders_number': {
                'read_only': True,
            },
            'favorites_number': {
                'read_only': True,
            },
            'date_created': {
                'read_only': True,
            },
        }


class CatalogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = [
            'id', 'parent', 'title', 'slug'
        ]
        depth = 2
