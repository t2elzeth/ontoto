import logging

from rest_framework import serializers

from . import models
from catalog.models import Product


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

    def create(self, validated_data: dict):
        request = self.context.get('request')

        user = request.user

        product = validated_data.get('product')
        favorite, _ = user.favorite.get_or_create(user=user)

        validated_data['user'] = user
        validated_data['favorite'] = favorite

        fp = models.FavoriteProduct.objects.create(**validated_data)
        return fp
