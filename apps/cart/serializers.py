import logging

from rest_framework import serializers

from . import models


class CartProductCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict):
        """Add user, his cart and final_price of products to validated data"""
        request = self.context.get('request')

        user = request.user
        if not user.is_authenticated:
            error = {
                'message': 'User is not authenticated'
            }
            return serializers.ValidationError(error)

        cart = user.cart.get_or_create(user=user, in_order=False)

        product = validated_data.get('product')
        qty = validated_data.get('qty')

        try:
            cp = cart.related_products.get(product=product)
            cp.qty = qty + cp.qty
            cp.save()
        except:
            validated_data['user'] = user
            validated_data['cart'] = cart
            cp = models.CartProduct.objects.create(**validated_data)
        return cp

    class Meta:
        model = models.CartProduct
        fields = [
            'product', 'qty'
        ]
