from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from . import serializers, models
from .permissions import IsOwner, CartIsNotInOrder


class CartProductListView(generics.ListAPIView):
    serializer_class = serializers.CartProductListSerializer
    queryset = models.CartProduct.objects.all()


class CartProductCreateView(generics.CreateAPIView):
    serializer_class = serializers.CartProductCreateRetrieveDestroySerializer
    permission_classes = [
        IsAuthenticated
    ]

    def perform_create(self, serializer):
        """Create new CartProduct object instance"""
        user = self.get_user()

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

    def get_user(self):
        return self.request.user


class CartProductDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = serializers.CartProductCreateRetrieveDestroySerializer
    queryset = models.CartProduct.objects.all()
    permission_classes = [
        IsOwner, CartIsNotInOrder
    ]
