import logging

from rest_framework import generics
from rest_framework.exceptions import ValidationError

from rest_framework import permissions

from cart.permissions import IsOwner

from . import models, serializers


class FavoriteProductListView(generics.ListAPIView):
    serializer_class = serializers.FavoriteProductListSerializer
    queryset = models.FavoriteProduct.objects.all()


class FavoriteProductCreateView(generics.CreateAPIView):
    serializer_class = serializers.FavoriteProductCreateSerializer
    queryset = models.FavoriteProduct.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def perform_create(self, serializer):
        # fp = serializer.save()
        user = self.request.user

        product = serializer.validated_data.get('product')

        favorite = user.favorite.first()
        queryset = favorite.related_favorites.filter(product__id=product.id)
        if queryset.exists():
            raise ValidationError(
                'Cannot add product to Favorites. It already exists there')
        serializer.save()


class FavoriteProductDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = serializers.FavoriteProductListSerializer
    queryset = models.FavoriteProduct.objects.all()
    permission_classes = [
        IsOwner
    ]
