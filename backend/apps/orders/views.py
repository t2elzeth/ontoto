from rest_framework import generics

from . import serializers, models


class OrdersListView(generics.ListAPIView):
    serializer_class = serializers.OrderListSerializer
    queryset = models.Order.objects.all()


class OrderCreateView(generics.CreateAPIView):
    serializer_class = serializers.OrderCreateSerializer

    def perform_create(self, serializer):
        user = self.get_user()

        cart = serializer.validated_data.get('cart')
        cart.in_order = True
        cart.save()

        for cp in cart.cart_products.all():
            cp.product.update_orders_number(save=True)

        is_gift = serializer.validated_data.get('is_gift')

        order = models.Order.objects.create(user=user, cart=cart, is_gift=is_gift)

        if is_gift:
            full_name = serializer.validated_data.get('full_name')
            email = serializer.validated_data.get('email')
            phone = serializer.validated_data.get('phone')
            address = serializer.validated_data.get('address')
            postal_code = serializer.validated_data.get('postal_code')

            models.Receiver.objects.create(
                order=order,
                full_name=full_name,
                email=email,
                phone=phone,
                address=address,
                postal_code=postal_code,
            )
        return order

    def get_user(self):
        return self.request.user


class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.OrderRetrieveUpdateDestroySerializer
    queryset = models.Order.objects.all()

    def perform_destroy(self, instance):
        receivers = instance.receivers.all()
        for receiver in receivers:
            receiver.delete()

        instance.delete()
