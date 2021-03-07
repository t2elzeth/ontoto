from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from . import models, serializers


class FavoriteProductViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FavoriteProductSerializer
    queryset = models.FavoriteProduct.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def perform_create(self, serializer):
        product = serializer.validated_data.get('product')

        favorite, _ = self.request.user.favorites.get_or_create(user=self.request.user)

        queryset = favorite.favorite_products.filter(product__id=product.id)
        if queryset.exists():
            raise ValidationError({'message': 'Cannot add product to Favorites. It already exists there'})
        serializer.save(user=self.request.user, favorite=favorite)

    def perform_destroy(self, instance: models.FavoriteProduct):
        product = instance.product
        instance.delete()
        product.count_favorites_number(save=True)
