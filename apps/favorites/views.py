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
        user = self.request.user

        product = serializer.validated_data.get('product')

        favorite = user.favorites.first()
        if favorite is None:
            favorite = models.Favorite.objects.create(user=user)

        queryset = favorite.favorite_products.filter(product__id=product.id)
        if queryset.exists():
            error = {
                'message': 'Cannot add product to Favorites. It already exists there'
            }
            raise ValidationError(error)
        serializer.save()


class FavoriteProductDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = serializers.FavoriteProductListSerializer
    queryset = models.FavoriteProduct.objects.all()
    permission_classes = [
        IsOwner
    ]
