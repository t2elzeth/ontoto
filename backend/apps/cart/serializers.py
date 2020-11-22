from rest_framework import serializers

from . import models


class CartProductCreateRetrieveDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartProduct
        fields = ['product', 'qty']


class CartProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartProduct
        fields = '__all__'
