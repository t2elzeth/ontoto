from rest_framework import serializers

from . import models


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartProduct
        fields = '__all__'
