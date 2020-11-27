from rest_framework import generics, permissions

from . import models, serializers


class ProductsListView(generics.ListAPIView):
    serializer_class = serializers.ProductListRetrieveUpdateDestroySerializer
    queryset = models.Product.objects.all()


class ProductCreateView(generics.CreateAPIView):
    serializer_class = serializers.ProductCreateSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProductListRetrieveUpdateDestroySerializer
    queryset = models.Product.objects.all()

    def perform_update(self, serializer):
        instance = self.get_object()

        if not instance.price == serializer.validated_data.get('price'):
            instance.set_old_price(save=True)

        return serializer.save()


class CategoryListView(generics.ListAPIView):
    serializer_class = serializers.CatalogListSerializer
    queryset = models.Category.objects.all()
