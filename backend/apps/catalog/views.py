from rest_framework import generics, permissions, viewsets

from . import models, serializers


class ProductViewSet(viewsets.ModelViewSet):
    serializers = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        if not self.get_object().price == serializer.validated_data.get('price'):
            serializer.validated_data.update({'old_price': self.get_object().price})
        serializer.save()


class CategoryListView(generics.ListAPIView):
    serializer_class = serializers.CatalogListSerializer
    queryset = models.Category.objects.all()
