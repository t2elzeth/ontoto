from django.shortcuts import render

from rest_framework import generics, permissions

from . import serializers, models
from .permissions import IsOwner


class CartProductListView(generics.ListAPIView):
    serializer_class = serializers.CartProductListSerializer
    queryset = models.CartProduct.objects.all()


class CartProductCreateView(generics.CreateAPIView):
    serializer_class = serializers.CartProductCreateOrDetailSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]


class CartProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CartProductCreateOrDetailSerializer
    queryset = models.CartProduct.objects.all()
    permission_classes = [
        IsOwner
    ]
