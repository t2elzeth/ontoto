from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from . import serializers, models
from .permissions import IsOwner, CartIsNotInOrder


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CartProductSerializer
    queryset = models.CartProduct.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'retrieve':
            return [IsAuthenticated, IsOwner, CartIsNotInOrder]

    def perform_create(self, serializer):
        """Create new CartProduct object instance"""
        user = self.request.user

        cart, _ = user.carts.get_or_create(user=user, in_order=False)

        product = serializer.validated_data.get('product')
        qty = serializer.validated_data.get('qty')

        cp, _ = cart.cart_products.get_or_create(product=product, defaults={'user': user, 'cart': cart})
        cp.qty += qty
        cp.save()
        return cp
