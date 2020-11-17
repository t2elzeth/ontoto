from rest_framework import serializers

from . import models


class FavoriteProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FavoriteProduct
        fields = [
            'id', 'product'
        ]


class FavoriteProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FavoriteProduct
        fields = [
            'product'
        ]

