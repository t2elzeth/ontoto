from rest_framework import generics

from . import serializers, models


class OrdersListView(generics.ListAPIView):
    serializer_class = serializers.OrderListRetrieveUpdateDestroySerializer
    queryset = models.Order.objects.all()


class OrderCreateView(generics.CreateAPIView):
    serializer_class = serializers.OrderCreateSerializer
    queryset = models.Order.objects.all()


class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.OrderListRetrieveUpdateDestroySerializer
    queryset = models.Order.objects.all()
