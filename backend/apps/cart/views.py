from rest_framework import generics, permissions

from . import serializers, models
from .permissions import IsOwner, CartIsNotInOrder


class CartProductListView(generics.ListAPIView):
    serializer_class = serializers.CartProductListSerializer
    queryset = models.CartProduct.objects.all()


class CartProductCreateView(generics.CreateAPIView):
    serializer_class = serializers.CartProductCreateRetrieveDestroySerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def perform_create(self, serializer):
        """
        Create new CartProduct object instance by adding
        `user`, `cart` to `validated_data`
        """

        user = self.request.user

        cart, _ = user.carts.get_or_create(user=user, in_order=False)

        product = serializer.validated_data.get('product')
        qty = serializer.validated_data.get('qty')

        cp, _ = cart.cart_products.get_or_create(
            product=product,
            defaults={
                'user': user,
                'cart': cart
            })
        cp.qty += qty
        cp.save()
        return cp


class CartProductDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = serializers.CartProductCreateRetrieveDestroySerializer
    queryset = models.CartProduct.objects.all()
    permission_classes = [
        IsOwner, CartIsNotInOrder
    ]
