from rest_framework import serializers

from . import models


class CartProductCreateOrDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartProduct
        fields = [
            'product', 'qty'
        ]

    def create(self, validated_data: dict):
        """
        Create new CartProduct object instance by adding 
        `user`, `cart` to `validated_data`
        """
        request = self.context.get('request')

        user = request.user

        cart, _ = user.carts.get_or_create(user=user, in_order=False)

        product = validated_data.get('product')
        qty = validated_data.get('qty')

        cp, _ = cart.cart_products.get_or_create(
            product=product,
            defaults={
                'user': user,
                'cart': cart
            })
        cp.qty += qty
        cp.save()
        return cp


class CartProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartProduct
        fields = '__all__'
