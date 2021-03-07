from rest_framework import serializers

from . import models


class FavoriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FavoriteProduct
        fields = [
            'id', 'product'
        ]
        read_only_fields = ['id']

